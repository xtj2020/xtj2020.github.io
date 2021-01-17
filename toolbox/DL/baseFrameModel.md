# 主要流程

1、构建数据集：训练集、验证集、测试集
2、shu'ju'ji


# 评价指标
- 混淆矩阵
| 预测值\真实值 |  Positive  | Negtive  |
|  ----  | ----  | ----  |
| Positive | TP |  FP |
| Negtive  | FN |  TN |



# 优化器
https://www.cnblogs.com/NeilZhang/p/8454890.html

- SGD

- SGDM

- Adagrad

- RMSProp

- Adam


<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

从线性回归-》感知机-》卷积神经网络-》循环神经网络

优化方法

统一符号与公式，看万家书，走自己路

# 训练基准代码

## 导入包

```python
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
import pandas as pd
import os
import inspect as ist
import shutil
import torch.nn as nn
import torchvision
import torch
import time
from PIL import Image
from tqdm import *
import torch.nn.functional as F
import math
import random
from torchvision import transforms,datasets,models
import torch.nn as nn
import torch.utils.data as data
from PIL import Image
from torch.utils.data.sampler import RandomSampler, SequentialSampler
##import img.transformer as transformer
import csv

import torchvision.transforms as transforms
from torch.autograd import Variable
```


## 数据类



### 数据加载器(采用datasets.ImageFolder方式)

```python
class Dataset:
    '''
属性：transform\train\data_images\data_images_loader\classes\classes_index
方法：get_item 返回值测试集图像和标签
    '''
    def __init__(self, train=True):
        self.transform = transforms.Compose([transforms.Resize((256, 256)),transforms.ToTensor(),
                                             transforms.Normalize(conf.mean, conf.std)
                                             ])
 
        self.train = train
        # 加载训练数据集和验证数据集
        if train:

            # 数据类型 data_images = {'train': xxx, 'valid': xxx}
            self.data_images = {x: datasets.ImageFolder(root=os.path.join(conf.root_data, x),
                                                        transform=self.transform)
                                for x in ['train', 'valid']}
            self.data_images_loader = {x: torch.utils.data.DataLoader(dataset=self.data_images[x],
                                                                      batch_size=conf.batch_size,
                                                                      shuffle=True)
                                       for x in ['train', 'valid']}
            # 图片分类 ['cat', 'dog']
            self.classes = self.data_images['train'].classes
            # 图片分类键值对 {'cat': 0, 'dog': 1}
            self.classes_index = self.data_images['train'].class_to_idx

        # 加载测试数据集
        else:
            images = [os.path.join(conf.test_data, img) for img in os.listdir(conf.test_data)]
            self.images = sorted(images, key=lambda x: int(x.split('.')[0].split('_')[0]))

#    重载专有方法__getitem__,该模块的目的只是为了获取测试图片(而且为验证集的图片)
    def __getitem__(self, index):
        img_path = self.images[index]
        label = int(self.images[index].split('.')[0].split('_')[0])
        data_images_test = Image.open(img_path)
        data_images_test = self.transform(data_images_test)
        return data_images_test, label

    # 重载专有方法__len__
    def __len__(self):
        return len(self.images)
    
dst = Dataset()
```


## 数据集的划分（移动到相应文件夹方法）

### 用csv文件作为标签读取，添加一列pd存储该行数据的情况

```python
len_small_csv = 3000

origin_csv = pd.read_csv('/home/xtu_conda/Downloads/DRD/trainLabels.csv')
small_csv = origin_csv.iloc[0:len_small_csv]
small_csv["usetype"] = None

#对csv中前3000个数据进行打乱
index_small_csv = np.arange(len(small_csv))
np.random.shuffle(index_small_csv)
len_train = 0.8*len(small_csv)
for i in range(len(small_csv)):
    if i < len_train:
        small_csv.loc[i,"usetype"] = "train"
    else:
        small_csv.loc[i,"usetype"] = "valid"

```


```python
#对文件的移动操作
if not os.listdir(os.path.join(conf.train_data,"0/")):    
    for i in range(len(small_csv)):
        subpath = small_csv.loc[i,"image"]+".jpeg"
        old_path = os.path.join(conf.root_train_data,subpath)
        sub_str = small_csv.loc[i,"usetype"]+r'/'+str(small_csv.loc[i,"level"])
        new_path = os.path.join(conf.root_data,sub_str)
#         print(old_path)
        shutil.copy(old_path,new_path)
```


### 对文件夹直接进行操作

```
trainFiles = os.listdir(os.path.join(conf.origin_dataset,'train/'))
dogFiles = list(filter(lambda x : x[:3] == "dog",trainFiles))
dogFiles=dogFiles[0:2500]
catFiles = list(filter(lambda x : x[:3] == "cat",trainFiles))
catFiles=catFiles[0:2500]
dogNum_train,catNum_train = len(dogFiles)*0.8,len(catFiles)*0.8


if not os.listdir(os.path.join(conf.train_dataset,'dog/')):    
    for i in range(len(dogFiles)):
        pre_path = os.path.join(conf.origin_dataset,'train/',dogFiles[i])
        if i < dogNum_train:
            new_path = os.path.join(conf.train_dataset,'dog/')
        else:
            new_path = os.path.join(conf.valid_dataset,'dog/')
        shutil.move(pre_path,new_path)

    for i in range(len(catFiles)):
        pre_path = os.path.join(conf.origin_dataset,'train/',catFiles[i])
        if i < catNum_train:
            new_path = os.path.join(conf.train_dataset,'cat/')
        else:
            new_path = os.path.join(conf.valid_dataset,'cat/')
        shutil.copy(pre_path,new_path)
```


```
pre_testset = os.listdir(os.path.join(conf.origin_dataset,'test/'))
pre_testset = pre_testset[0:1249]
new_path = conf.test_dataset
for i in range(len(pre_testset)):
    pre_path = os.path.join(conf.origin_dataset,'test/',pre_testset[i])
    shutil.copy(pre_path,new_path)
```


## 配置文件

### 配置内容

```
class config:
    root_train_data = '/home/xtu_conda/xtjdata/DRD/train/'
    root_data = '/home/xtu_conda/xtjdata/small-DRD/'
    train_data = '/home/xtu_conda/xtjdata/small-DRD/train/'
    test_data = '/home/xtu_conda/xtjdata/small-DRD/test/'
    label_csv = '/home/xtu_conda/xtjdata/small-DR/trainLabels.csv'
    
    mean = [0.3219411 , 0.22811799, 0.16616374]
    std =[0.15051048, 0.10913553, 0.0876774 ]
    batch_size = 16
    
conf = config() 
```


### 获取图片的均值

获取图像的均值与方差的前提是要对图像进行加载

```python
def get_mean_std(data_images):
    times, mean, std = 0, 0, 0
    data_loader = {x: torch.utils.data.DataLoader(dataset=data_images[x],
                                                  batch_size=1000,
                                                  shuffle=True)
                          for x in ['trainData', 'validData']}
    for imgs, labels in data_loader['trainData']:
        # imgs.shape = torch.Size([32, 3, 64, 64])
        times += 1
        mean += np.mean(imgs.numpy(), axis=(0, 2, 3))
        std += np.std(imgs.numpy(), axis=(0, 2, 3))
        print('times:', times)

    mean /= times
    std /= times
    return mean, std

dataset=Dataset()
get_mean_std(dataset.data_images)
```


## 统计与可视化分析

### 标签类别数目的统计

使用文件夹的形式

```python
pic_list = os.listdir('/home/xtu_conda/Downloads/DRD/test/')
a = len(pic_list)
```


使用csv的形式

### 对图片的展示

```python
import torchvision
import cv2

imgs, labels = iter(dst.data_images_loader['train']).next() 
# 制作雪碧图
# 类型为tensor，维度为[channel, height, width]
img = torchvision.utils.make_grid(imgs)
# 转换为数组并调整维度为[height, width, channel]
img = img.numpy().transpose([1, 2, 0])
# 通过反向推导标准差交换法计算图片原来的像素值
mean, std = conf.mean, conf.std
img = img * std + mean
# 打印图片标签
print([dst.classes[i] for i in labels])
# 显示图片
# cv2.imshow('img', img)
# # 等待图片关闭
# cv2.waitKey(0)

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
# cat = mpimg.imread(img)
# print(cat.shape) 
plt.imshow(img) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
```


## 模型与网络(用过的，计入代码基准的)



## 训练与验证

## 训练（独立的）

## 验证（独立的）

## 测试





# 基本术语

带有集成字样的是对目前所学内容的集成

## 线性回归

x真实值 y标签值。
$\large \hat y$预测值

$ l^{(i)}$ 损失函数 $l(x)$代价函数

## 多元感知机

样本$\large X\in\mathbb R^{n*d} $,批量大小为n,输入个数为d,

输入层为$x_i$,隐藏层为$h_i$,输出层为$o_i$

隐藏层权重参数$\large W_h \in \mathbb R^{d \times h} $和偏差参数$\large b_h \in \mathbb R^{1 \times h}$,
隐藏单元个数为h,输出为H，$H \in \mathbb R^{n \times h}$
输出层权重参数$\large W_o \in \mathbb R^{d \times q}$和偏差参数$\large b_h \in \mathbb R^{1 \times h}$。
$\eta$学习率 batch epoch
$\phi$为激活函数

## 神经网络

# 线性回归

## 数据

### 数据的生成

$y = X{\mathcal w}+b+ \epsilon$

$\epsilon$代表着干扰，服从均值为0，标准查为0.01的正态分布,真实${\mathbb w}$的取值为$[2,-3.4]^T$,偏差b=4.2。

$X \in {\mathbb R}^{100 \times 2} $,X为矩阵，其中上标1000的含义为1000个样本，2为2列，即2个影响因素，相对于是一个向量。100*2表示特征。

```python
feature = tensor.randn(1000,2,dtype=float32) #生成干扰项
torch.tensor(np.random.normal((0,0.01,size = labels.size()),dtype=float32)
```


```
torch.rand均匀分布
torch.randn标准正态分布
torch.normal(mean,std,size)离散正态分布
torch.linespace(start,end,steps=100)

numpy.random.rand(d0,d1,…,dn)
函数根据给定维度生成[0,1)之间的数据，包含0，不包含1
dn表格每个维度
返回值为指定维度的array

random.randint()给定范围的整数
random.random()返回0与1之间的浮点数字，不接受参数
```


### 数据的表示

```python
pylot使用rc配置文件来自定义图形的各种默认属性，称之为rc配置或rc参数。通过rc参数可以修改默认的属性，包括窗体大小、每英寸的点数、线条宽度、颜色、样式、坐标轴、坐标和网络属性、文本、字体等。
import numpy as np
import matplotlib.pyplot as plt
###%matplotlib inline    #jupyter可以用，这样就不用plt.show()

#生成数据
x = np.linspace(0, 4*np.pi)
y = np.sin(x)
#设置rc参数显示中文标题
#设置字体为SimHei显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#设置正常显示字符
plt.rcParams['axes.unicode_minus'] = False
plt.title('sin曲线')
#设置线条样式
plt.rcParams['lines.linestyle'] = '-.'
#设置线条宽度
plt.rcParams['lines.linewidth'] = 3
#绘制sin曲线
plt.plot(x, y, label='$sin(x)$')

plt.savefig('sin.png')
plt.show()
```


```python
def use_svg_display():
    # 用矢量图显示
    display.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    # 设置图的尺寸
    plt.rcParams['figure.figsize'] = figsize

set_figsize()
plt.scatter(features[:, 1].numpy(), labels.numpy(), 1);

```


### **读取小批量**

利用迭代器来获取每次小批量的数据：先打乱，然后取步长为批量处理数来对样本进行抽样。

longtersor相当于长整形

```
def data_iter(bath_size,features,labels):
	num_samples = len(features)
	indices=list(range(num_samples)
	for i in num_samples
```


```
yield  features.index_select(0, j), labels.index_select(0, j)
```


==因为只有一个维度，为什么产生的这个维度？==

## 定义模型与初始化

torch.mul(a,b)对应位相乘

torch.mm(a,b)矩阵相乘

```python
def linreg(X,w,b):
	return torch.mm(X,w)+b
```


==需要知道返回的是什么样的数据==



数值的初始化

```python
w=torch.tensor(np.normal(0,0.01,(num_inputs,1)),dytpe=torch.float32)
b=torch.zeros(1,dtype=torch.float32)
```


加入梯度

```
w.requires_grad_(requires_grad=True)
b.requires_grad_(requires_grad=True)
```


## 损失函数与代价函数

### 能够计算的基础条件

损失函数（Loss Function ）是定义在单个样本上的，算的是一个样本的误差。
代价函数（Cost Function ）是定义在整个训练集上的，是所有样本误差的平均，也就是损失函数的平均。
代价函数的两个假设：
1、代价函数可以被写成一个每个训练样本x上的代价函数$C_x$的均值$C={1 \over n}\sum_xC_x$;
2、代价函数可以写成神经网络输出的函数：
$C={1 \over 2}\lVert y -a ^L \rVert ^2 ={1 \over 2}{\sum_j(y_j-a^L_j)^2}$

单个误差$\Large \mathcal l^{(i)}(w_1,w_2,b)={1 \over 2} ({\hat y^{(i)} -y^{(i)} )^2}$叫损失函数。

总的误差$\Large \mathcal l(w_1,w_2,b)={1 \over n}{\sum_{i=1}^n(\hat y - y)^2}$叫代价函数。

```python
#这里计算的是单个的损失函数
def suqared_loss(y_hat,y):
	return (y_hat-y.view(y_hat.size()))**2/2
```


### 交叉熵损失函数

为了解决刚开始的学习缓慢的问题，$\sigma$函数会逐渐变得很平缓。导致偏导数过小。以及后面的梯度消失问题，也就是一般神经网络学习缓慢的原因。

能够作为交叉熵的条件：
1、它是非负的，C>0,而且定义域为（0，1）；
2、对于所有输入x，实际的输出接近目标值，交叉熵接近于0

公式为：$\large H(y^{(i)},\hat y^{(i)})=-\sum_{j=1}^qy_j^{(i)}log \hat y_j^{(i)}$

n个样本的交叉熵
$\Large \mathcal l（ \boldsymbol\Theta）={1 \over n}\sum_{i=1}^nH(y^{(i)},\hat y^{(i)})$

## 优化算法

我们需要将求得代价函数的最小值，这样就转换为了一个最优化的问题。即如何更新权重使得代价函数最小。

能够用公式直接计算出来的称为解析解，通过数值模拟的方法计算出来的叫数值解

由于参数过多导致计算需要的资源过多，于是采用小批量的方法简化运算。

### 一种理论模型

我们要求某个地势上的一个最小点，利用一个球的滚动去求这个点。
这个最小点为C,地势的变化为$\triangle C$ ，$\nabla C$为地势的方向，$\triangle v$为球的位置变化，球由地势进行小梯度地下降。

### 动手实践的理论与代码

能进行反向传播的基础：$\triangle output \approx \sum_j {\partial output \over \partial w_j}\triangle w_j + {\partial output \over \partial b}\triangle b$

$\Large w_1 \leftarrow w_1 - {\eta \over \lvert \mathcal{B}\rvert}\sum_{i \in \mathcal{B}}{\partial l^{(i)}(w_1,w_2,b)\over \partial w_1} $
$\Large w_2 \leftarrow w_2 - {\eta \over \lvert \mathcal{B}\rvert}\sum_{i \in \mathcal{B}}{\partial l^{(i)}(w_1,w_2,b)\over \partial w_2} $
$\Large b \quad \leftarrow b \quad - {\eta \over \lvert \mathcal{B}\rvert}\sum_{i \in \mathcal{B}}{\partial l^{(i)}(w_1,w_2,b)\over \partial b} $

```python
def sgd(params,lr,batch_size):
    for param in params:
        param.data -= lr*param.grad /batch_size
	# 这里自动求梯度模块计算得来的梯度是一个批量样本的梯度和。
    #在加入梯度的过程中就赋予了param.grad，
```


## 训练模型

epoch为迭代模型的周期

```python
lr=0.03
net=linereg
loss=squared_loss
optimier=sgd
#这里用的是小批量梯度下降，那么对数据的提取又是一种什么样的情况呢？
#可以理解为每处理一批，计算一次损失函数，并对其进行一次反向传播
for epoch in range(num_epoch):
    for x,y in data_liter:
		l=loss(net(w_1,w_2,b),y).sum()
        l.backward#小批量的损失对模型参数求梯度
        sgd([w,b],lr,batch_size)#sgd对应小批量随机梯度下降迭代模型参数
        
        w.grad.data.zero_()
        b.grad.data.zero_()
     train_l =loss(net(feature,w,b),labels)
     print('epoch %d,loss %f' % (epoch+1,train_l.mean().item())
    

```


### 导入包中数据

**torchvision包**
torchvision.datasets
torchvision.models
torchvision.transforms
torchvison.utils

**获取数据集**

```
torchvision.dataset.FasionMNIST(root="",train =True,download=Ture,transform=transform.toTensor())
```


# 改为softmax

线性回归的局限性：只能够预测一个连续值，不能够进行分类。
我们需要一个能够进行分类的，并能够给出分类概率的学习网络。softmax能够将输出值变换成值为正且和为1的概率分布。



### 定义模型与初始化

### softmax的实现

softmax公式

$\huge \hat y_i = {e^{(o_i)} \over \sum_i^n e^{(o_i)}}$

### 模型

### 损失函数-交叉熵



### 计算准确率

### 训练模型

### 预测

# 多层感知机

### 全链接层



### 激活函数

#### ReLU函数

只保留正数元素，而不保留负数（就负数元素清零）。

ReLU(x)=max(x,0)

```python
def relu(x):
    return torch.max(input,other=torch.tensor(0,0))
```


#### sigmoid函数

可以将元素变为0和1之间,进一步可以控制信息在神经网络中的流动。
当输入为0时，sigmoid函数的导数达到最大值0.25；当输入越偏离0时，sigmoid函数的导数越接近0。

$\Large sigmoid \ x = {1 \over {1+exp(-x)}}$

![img](baseFrameModel.assets/3.8_sigmoid_grad.png)

#### tanh函数

可以将元素变换到-1和1之间

$\Large tanh(x)={ 1-exp(-2x)\over 1+exp(-2x)} $

### 模型

$H=\phi(XW_h+b_h)$
$O=HW_o+b_o$

### 定义损失函数

### 训练模型

# 模型的进一步优化

# 卷积神经网络

## 卷积层

### 二维互相关函数

```python
def corr2d(X,K):
	h,w = k.shape
	Y = torch.zero(x.shape[0]-h+1,X.shape[1]-w+1)
	for i in range(Y.shape[0]):
		for j in range(Y.shape[1]):
			Y[i,j]=(x[i:i+h,j:j+w]*k).sum()
    return Y
```


### 二维卷积层

将输入和卷积核做互相关运算，并加上一个标量偏差来得到输出。

```
class Con2D(nn.Module):
	def __init__(sel,kernel_size):
		super(Conv2D,self).__init__()
		self.weight == nn.Parameter(torch.-randn(kernel_size))
		self.bias = nn.Paramter(torch.randn(1))
	def forward(self,x):
		return corr2d(x,self.wight)+self.bias
```


### 模拟边缘检测

### 通过数据学习核数组

### 卷积与互关函数的区别

### 特征图与感受野

输入在空间维度（宽和高）上某一级的表征，也叫特征图（feature map）。

## 池化层



# 循环神经网络

## 语言模型与计算公式

$\large p(w_1,w_2,...,w_t)=\prod_i^TP(w_t\vert w_1,...,w_t-1)$

时间步长t的词$w_t$对基于前面所有词的条件概率只考虑了最近时间步的n−1个词。如果要考虑比t−(n−1)更早时间步的词对$w_t$的可能影响，我们需要增大n。但这样模型参数的数量将随之呈指数级增长。

循环神经网络并非固定记忆，而是通过隐藏层来存储同步之前的时间步的信息。

### n元语法





## 反向传播的工作

目标函数（Object Function）定义为：最终需要优化的函数。等于经验风险+结构风险（也就是Cost Function + 正则化项）。



四个基本方程：
1、

## 解释梯度下降

## 证明深度学习能够拟合任意函数

# pytorch库的实现

$\large \begin{equation} p = \sum_{n=1}^Na_n \end{equation}$

$\large p = \sum\limits_{n=1}^Na_n$

# 计算神经网络的像素大小



Width=(W-F+2P)/S+1

Height=(H-F+2P)/S+1

池化层计算公式



# 参考文献
[动手实现]: https://tangshusen.me/Dive-into-DL-PyTorch/#/	"动手实现深度学习"
[无痛的机器学习]:https://zhuanlan.zhihu.com/p/23776390 "无痛的深度学习"
