基本数据类型

ndarray:存储单一数据类型的多维数组

ufunc：能对数组进行处理的函数

## 创建


- np.array(列表、元组、镶嵌列表)
- np.arange() 通过指定开始值、终值和步长来创建一维数组，注意数组不包括终值
- np.linspace() 开始值、终值和元素个数，默认包含终值，endpoin也可指定
- zeros()、ones()、empty()、zeros_like()、ones_like()、empty_like()

```python
c.dtype #获得numpy的元素类型
c.shape #获得数组的大小
```

数组取值：
a[3:5] 含下界不含上界
步长为负数时，开始下标必须大于结束下标

和Python的列表序列不同，通过下标范围获取的新的数组是原始数组的一个视图。它与原始数组共享同一块数据空间

```python
 x[[3, 3, 1, 8]] # 获取x中的下标为3, 3, 1, 8的4个元素，组成一个新的数组
```

当使用布尔数组作为下标存取数组x中的元素时，将收集数组x中所有在布尔数组中对应下标为True的元素。使用布尔数组作为下标获得的数组不和原始数组共享数据空间，注意这种方式只对应于布尔数组，不能使用布尔列表。

当使用整数序列对数组元素进行存取时，将使用整数序列中的每个元素作为下标，整数序列可以是列表或者数组。使用整数序列作为下标获得的数组不和原始数组共享数据空间。

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

# 对数组的拼接操作

numpy.dstack 将列表中的数组沿深度方向进行拼接。

np.stack()

np.hstack()

np.vstack()

np.dstack()

<https://blog.csdn.net/fripy/article/details/86658002>

# 维度的转换
ravel()
flatten，与ravel相同，区别在是否拷贝

# 排序

np.argsort(x)与np.sort()



