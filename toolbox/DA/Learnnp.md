基本数据类型

ndarray:存储单一数据类型的多维数组

ufunc：能对数组进行处理的函数

## 创建

```python
c=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
c.dtype #获得numpy的元素类型
c.shape #获得数组的大小
```

当某个轴的元素为-1时，将会根据元素自动计算轴的长度。

reshape可以创建一个改变了尺寸的新数组，原数组不变。同时新数组和原数组共享数据内存空间，改变其中一个会改变另一个。

## 矩阵运算

对于多维数组，在缺省情况下使用矩阵运算，提供matrix对象以进行矩阵运算

矩阵的乘积可以使用dot函数进行运算

## 文件存储

二进制（分Numpy专用格式和无格式）与文本

tofile以二进制无格式写入文件，用numpy.fromfile读取回来需要自己格式化数据

## 生成随机数（所生成的随机数为列表形式）

##### numpy.random.rand(d0,d1,…,dn)

- rand函数根据给定维度生成[0,1)之间的数据，包含0，不包含1
- dn表格每个维度
- 返回值为指定维度的array

##### numpy.random.randn(d0,d1,…,dn)

- randn函数返回一个或一组样本，具有标准正态分布。
- dn表格每个维度
- 返回值为指定维度的array

##### np.random.seed()

- 的作用：使得随机数据可预测。
- 当我们设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数

##### numpy.random.choice(a, size=None, replace=True, p=None)

- 从给定的一维数组中生成随机数
- 参数： a为一维数组类似数据或整数；size为数组维度；p为数组中的数据出现的概率
- a为整数时，对应的一维数组为np.arange(a)

##### 生成[0,1)之间的浮点数

- numpy.random.random_sample(size=None)
- numpy.random.random(size=None)
- numpy.random.ranf(size=None)
- numpy.random.sample(size=None)

##### numpy.random.randint(low, high=None, size=None, dtype=’l’)

- 返回随机整数，范围区间为[low,high），包含low，不包含high
- 参数：low为最小值，high为最大值，size为数组维度大小，dtype为数据类型，默认的数据类型是np.int
- high没有填写时，默认生成随机数的范围是[0，low)

np.random.shuffle(x) 类似洗牌，打乱顺序；np.random.permutation(x)返回一个随机排列