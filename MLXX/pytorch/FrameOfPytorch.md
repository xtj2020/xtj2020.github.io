# 数据的准备

## 数据的加载

```python
from Torchvison import datasets,transforms
x_train = datasets.fashionMNIST(root = '../datasets',train = True,transorms.ToTensor(),download = True)
```



## 数据的预处理

### 归一处理



# 网络配置

## 网络搭建

```python
class net_name (nn.Mudel)：#M必需为大写
	def __init__(self):
    super(net_name,self).__init__()
    self.conv1 = nn.linear()
  def forward(self,x):
    out = self.conv1(x)
    return out
```



### Nn.Module的继承

### 网络结构

### 定义前向传播

## 实例化

## 定义损失函数和优化器

```python
criterion = nn.MSELoss()
optimzer = optim.SGD(  )
```



# 网络训练

## 前向传播

## 后向传播

## 打印与保存

# 网络预测