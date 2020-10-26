从线性回归-》感知机-》卷积神经网络-》循环神经网络

优化方法

# 线性回归

自己模拟数据进行房价的预测

## 模型

## 数据

$y = X{\mathcal w}+b+ \epsilon$

$\epsilon$代表着干扰，服从均值为0，标准查为0.01的正态分布,真实${\mathbb w}$的取值为$[2,-3.4]^T$,偏差b=4.2。

$X \in {\mathbb R}^{100*2} $,X为矩阵，其中上标1000的含义为1000个样本，2为2列，即2个影响因素，相对于是一个向量。100*2表示特征。

 ==如何使用pytorch实现数据的模拟？==

```python
feature = tensor.randn(1000,2,dtype=float32) 
#生成干扰项
torch.tensor(np.random.normal((0,0.01,size = labels.size()),dtype=float32)
```

## 读取数据

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

==为什么只选取第一个维度的数据==
==因为只有一个维度，为什么产生的这个维度？==

弄清f

[动手实现]: https://tangshusen.me/Dive-into-DL-PyTorch/#/	"动手实现深度学习"

## 初始化模型

数值的初始化

加入梯度

## 定义模型

torch.mul(a,b)对应位相乘

torch.mm(a,b)矩阵相乘

```python
def linreg(X,w,b):
	return torch.mm(X,w)+b
```

==需要知道返回的是什么样的数据==

## 定义损失函数与优化算法



## 训练模型

epoch为迭代模型的周期

# 改为softmax

线性回归的局限性：只能够预测一个连续值，不能够进行分类。
我们需要一个能够进行分类的，并能够给出分类概率的学习网络。softmax能够将输出值变换成值为正且和为1的概率分布。

## 数据的读取

## 初始化模型参数

## softmax的实现

## 模型

## 损失函数

## 计算准确率

## 训练模型

## 预测

# 多层感知机

# 卷积神经网络

# 循环神经网络