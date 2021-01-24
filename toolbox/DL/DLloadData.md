# 数据预处理
**进行数据的统计分析:**
只有对数据的足够了解，有针对性筛选出合适的数据进行训练，才能有效得到实验效果。

1、数据的可视化； \
2、缺失数据与重复数据的处理； \
3、多标签数据的处理；



**训练数据预处理：**考虑训练网络数据的输入要求

将数据预期处理，将其固化入（pkl文件\hdf5文件）中


# Dataset类与DataLoader

```python
batch_size = 16
class Dataset:
    def __init__(self, train=True):
        self.train = train
        # 加载训练数据集
        if train:
            pkl_file = open('../../xtjtemp/RF_feature48_train_pic_list.pkl', 'rb')
            self.train_list = pickle.load(pkl_file) #[ID名，标签，图片] 

        # 加载测试数据集
        else:
            pkl_file = open('../../xtjtemp/RF_feature48_dev_pic_list.pkl', 'rb')
            self.dev_list = pickle.load(pkl_file) #[ID名，标签，图片]
            
            
    # 获取单条数据，同时将数据转化成为Tensor输入
    def __getitem__(self, index):
        if self.train:
            data_pic = self.train_list[2][index-1] #该数据类型为列表，需要对其转为矩阵，并转为tensor数据类型
            data_images = torch.from_numpy(np.array(data_pic)+0.0/255).float()
#           data_images = torch.from_numpy(np.array(data_pic).transpose(2,0,1)/255).float()
            label_pic = self.train_list[1][index-1]
            label_imagae = torch.from_numpy(np.array(label_pic)).long()
            data_id = self.train_list[0][index-1]
        else:
            data_pic = self.dev_list[2][index-1] #该数据类型为列表，需要对其转为矩阵，并转为tensor数据类型
            data_images = torch.from_numpy(np.array(data_pic)+0.0/255).float()
#             data_images = torch.from_numpy(np.array(data_pic).transpose(2,0,1)/255).float()
            label_pic = self.dev_list[1][index-1]
            label_imagae = torch.from_numpy(np.array(label_pic)).long()
            data_id = self.dev_list[0][index-1]
        return data_id,data_images, label_imagae 

    # 重载专有方法__len__
    def __len__(self):
        if self.train:
            return len(self.train_list[2])
        else:
            return len(self.dev_list[2])
    
train_dst = Dataset(train=True)
train_loader = DataLoader(train_dst, batch_size=16, shuffle=True)

dev_dst = Dataset(train=False)
dev_loader = DataLoader(dev_dst, batch_size=16, shuffle=True)
```


可以查看数据

```python
# enumerate 返回的是索引以及迭代器的迭代值
for i, data in enumerate(datas):
	# i表示第几个batch， data表示该batch对应的数据，包含data和对应的labels
    print("第 {} 个Batch \n{}".format(i, data))
```

