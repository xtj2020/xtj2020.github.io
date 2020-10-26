从线性回归-》感知机-》卷积神经网络-》循环神经网络

优化方法

# 代码框架

## 线性回归

自己模拟数据进行房价的预测

### 数据

#### 数据的模拟与生成

$y = X{\mathcal w}+b+ \epsilon$

$\epsilon$代表着干扰，服从均值为0，标准查为0.01的正态分布,真实${\mathbb w}$的取值为$[2,-3.4]^T$,偏差b=4.2。

$X \in {\mathbb R}^{100*2} $,X为矩阵，其中上标1000的含义为1000个样本，2为2列，即2个影响因素，相对于是一个向量。100*2表示特征。

```python
feature = tensor.randn(1000,2,dtype=float32) 
#生成干扰项
torch.tensor(np.random.normal((0,0.01,size = labels.size()),dtype=float32)
```

```
torch.rand均匀分布
torch.randn标准正态分布
torch.normal(mean,std,size)离散正态分布
torch.linespace(start,end,steps=100)
```



#### 读取数据

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

### 定义模型

torch.mul(a,b)对应位相乘

torch.mm(a,b)矩阵相乘

```python
def linreg(X,w,b):
	return torch.mm(X,w)+b
```

==需要知道返回的是什么样的数据==

### 初始化模型

数值的初始化

```

```

加入梯度

```
w
```

### 损失函数与代价函数

单个误差$\mathcal l^{(i)}(w_1,w_2,b)={1 \over 2} ({\hat y^{(i)} -y^{(i)} )^2}$

总的误差$\mathcal l(w_1,w_2,b)={1 \over n}{\sum_{i=1}^n(\hat y - y)^2}$

```python
def suqared_loss(y_hat,y):
	return (y_hat-y.view(y_hat.size()))**2/2
```

### 优化算法

能够用公式直接计算出来的称为解析解，通过数值模拟的方法计算出来的叫数值解

参数的迭代（小批量）

$$\Large w_1 \leftarrow w_1 - {\eta \over \lvert \mathcal{B}\rvert}\sum_{i \in \mathcal{B}}{\partial l^{(i)}(w_1,w_2,b)\over \partial w_1} $$
$$\Large w_2 \leftarrow w_2 - {\eta \over \lvert \mathcal{B}\rvert}\sum_{i \in \mathcal{B}}{\partial l^{(i)}(w_1,w_2,b)\over \partial w_2} $$
$$\Large b \quad \leftarrow b \quad - {\eta \over \lvert \mathcal{B}\rvert}\sum_{i \in \mathcal{B}}{\partial l^{(i)}(w_1,w_2,b)\over \partial b} $$

```python
def sgd(params,lr,batch_size):
    for param in params:
        param.data -= lr*param.grad /batch_size
	# 这里自动求梯度模块计算得来的梯度是一个批量样本的梯度和。
```

### 训练模型

epoch为迭代模型的周期

```

```



## 改为softmax

线性回归的局限性：只能够预测一个连续值，不能够进行分类。
我们需要一个能够进行分类的，并能够给出分类概率的学习网络。softmax能够将输出值变换成值为正且和为1的概率分布。

### 数据的读取

### 初始化模型参数

### softmax的实现

softmax公式

$\hat y_i = {e^{(0_i)} \over \sum_i^n e^{(o_i)}}$

### 模型

### 损失函数

### 计算准确率

### 训练模型

### 预测

## 多层感知机

## 卷积神经网络

## 循环神经网络

# 凸优化

## 反向传播的工作

能进行反向传播的基础

$\triangle output \approx \sum_j {\partial output \over \partial w_j}\triangle w_j + {\partial output \over \partial b}\triangle b$

一个纯粹的理论模型

### 定义

损失函数（Loss Function ）是定义在单个样本上的，算的是一个样本的误差。

代价函数（Cost Function ）是定义在整个训练集上的，是所有样本误差的平均，也就是损失函数的平均。
代价函数的两个假设：
1、代价函数可以被写成一个每个训练样本x上的代价函数$C_x$的均值$C={1 \over n}\sum_xC_x$;
2、代价函数可以写成神经网络输出的函数：
$C={1 \over 2}\lVert y -a ^L \rVert ^2 ={1 \over 2}{\sum_j(y_j-a^L_j)^2}$

目标函数（Object Function）定义为：最终需要优化的函数。等于经验风险+结构风险（也就是Cost Function + 正则化项）。



四个基本方程：
1、

## 解释梯度下降

## 证明深度学习能够拟合任意函数

# pytorch库的实现

# 参考文献
[动手实现]: https://tangshusen.me/Dive-into-DL-PyTorch/#/	"动手实现深度学习"