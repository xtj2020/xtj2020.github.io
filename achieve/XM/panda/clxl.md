## 描述

在这次竞赛中，我发现了许多公共内核可以直接将输入图像缩放为正方形。但是，对于此特定数据，这种方法不是很有效，因为所提供图像的纵横比和大小不一致，并且变化范围很大。结果，输入图像以不一致的方式向上扩展，从而大大扩展了变形，从而限制了模型的学习能力。此外，输入包含较大的空白区域，导致GPU内存和GPU时间的使用效率低下。

在此内核中，我提出了一种基于串联切片池的替代方法。无需传递整个图像作为输入，而是根据组织像素的数量从每个图像中选择N个图块（有关数据准备和相应数据集的描述，请参阅此内核），并独立地通过卷积部分。对于池化和FC头之前的每个图像，将卷积部分的输出串联在一个大的单个图中（请参见下图）。由于池化层消除了任何空间信息，因此Concat Tile池化方法几乎等同于将整个图像传递给卷积部分，不包括对几乎没有空域的预测（对最终预测无贡献的预测），并对其余输出进行混洗变成较小尺寸的正方形地图。下面，我仅提供一个基本内核，仅说明此方法。在我的第一个试验中，我获得了0.76磅的得分，目前排名前2位，我相信它可以很容易地提高到0.80+。希望您喜欢我的内核，也请检查实现基于图块方法的提交内核。

<img src="https://i.ibb.co/hF6LRVm/TILE.png" alt="img" style="zoom: 200%;" />

```python
sz = 128
bs = 32
nfolds = 4
SEED = 2020
N = 12 #number of tiles per image
TRAIN = '../input/panda-16x128x128-tiles-data/train/'
LABELS = '../input/prostate-cancer-grade-assessment/train.csv'

```

## DATA

使用分层的KFold拆分。

```python
df = pd.read_csv(LABELS).set_index('image_id')
files = sorted(set([p[:32] for p in os.listdir(TRAIN)]))
df = df.loc[files]
df = df.reset_index()
splits = StratifiedKFold(n_splits=nfolds, random_state=SEED, shuffle=True)
splits = list(splits.split(df,df.isup_grade))
folds_splits = np.zeros(len(df)).astype(np.int)
for i in range(nfolds): folds_splits[splits[i][1]] = i
df['split'] = folds_splits
df.head()
```

检查此内核以获取图像统计信息。由于我使用零填充并且背景对应于255，因此在加载图像时会将图像反转为255-img。
因此，平均值计算为“ 1- val”。

```python
mean = torch.tensor([1.0-0.90949707, 1.0-0.8188697, 1.0-0.87795304])
std = torch.tensor([0.36357649, 0.49984502, 0.40477625])
```

下面的代码（在隐藏的单元格中）创建能够加载图像的多个图块的ImageItemList。它专用于fast.ai，而且纯Pytorch代码会简单得多。

```python
def get_data(fold=0):
    return (MImageItemList.from_df(df, path='.', folder=TRAIN, cols='image_id')
      .split_by_idx(df.index[df.split == fold].tolist())
      .label_from_df(cols=['isup_grade'])
      .transform(get_transforms(flip_vert=True,max_rotate=15),size=sz,padding_mode='zeros')
      .databunch(bs=bs,num_workers=4))

data = get_data(0)
data.show_batch()
```

## model

下面的代码实现了Concat Tile池化思想。作为骨干，我使用半弱监督ImageNet预训练的ResNeXt50模型，该模型在以前的许多比赛中对我都非常有效。

```python
class Model(nn.Module):
    def __init__(self, arch='resnext50_32x4d_ssl', n=6, pre=True):
        super().__init__()
        m = torch.hub.load('facebookresearch/semi-supervised-ImageNet1K-models', arch)
        self.enc = nn.Sequential(*list(m.children())[:-2])       
        nc = list(m.children())[-1].in_features
        self.head = nn.Sequential(AdaptiveConcatPool2d(),Flatten(),nn.Linear(2*nc,512),
                            Mish(),nn.BatchNorm1d(512), nn.Dropout(0.5),nn.Linear(512,n))
        
    def forward(self, *x):
        shape = x[0].shape
        n = len(x)
        x = torch.stack(x,1).view(-1,shape[1],shape[2],shape[3])
        #x: bs*N x 3 x 128 x 128
        x = self.enc(x)
        #x: bs*N x C x 4 x 4
        shape = x.shape
        #concatenate the output for tiles into a single map
        x = x.view(-1,n,shape[1],shape[2],shape[3]).permute(0,2,1,3,4).contiguous()\
          .view(-1,shape[1],shape[2]*n,shape[3])
        #x: bs x C x N*4 x 4
        x = self.head(x)
        #x: bs x n
        return x
```

## Training

```python
fname = 'RNXT50'
pred,target = [],[]
for fold in range(nfolds):
    data = get_data(fold)
    model = Model()
    learn = Learner(data, model, loss_func=nn.CrossEntropyLoss(), opt_func=Over9000, 
                metrics=[KappaScore(weights='quadratic')]).to_fp16()
    logger = CSVLogger(learn, f'log_{fname}_{fold}')
    learn.clip_grad = 1.0
    learn.split([model.head])
    learn.unfreeze()

    learn.fit_one_cycle(16, max_lr=1e-3, div_factor=100, pct_start=0.0, 
      callbacks = [SaveModelCallback(learn,name=f'model',monitor='kappa_score')])
    torch.save(learn.model.state_dict(), f'{fname}_{fold}.pth')
    
    learn.model.eval()
    with torch.no_grad():
        for step, (x, y) in progress_bar(enumerate(data.dl(DatasetType.Valid)),
                                     total=len(data.dl(DatasetType.Valid))):
            p = learn.model(*x)
            pred.append(p.float().cpu())
            target.append(y.cpu())
```

```python
p = torch.argmax(torch.cat(pred,0),1)
t = torch.cat(target)
print(cohen_kappa_score(t,p,weights='quadratic'))
print(confusion_matrix(t,p))
```