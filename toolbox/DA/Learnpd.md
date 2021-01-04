# 展示与统计信息


df.head(10)
df.info()
type(df[1])
df.dtypes


## 排序
.sort_index()方法在指定轴上根据索引进行排序，默认升序
.sort_index(axis=0, ascending=True)

df.index    行名称
df.columns  列名称
df._info_axis_     列名称

（bike1，bike2）=df.shape  行、列高度
len(df)    输出的是行高
df.index.size    行高
df.columns.size   列高



## pd显示

pd.set_option('display.width', 200)   # 横向最多显示多少个字符， 一般80不适合横向的屏幕，平时多用200.pd.set_option('display.max_columns', 12)
 pd.set_option('display.max_rows', 10)  # 显示的最大行数和列数
pd.set_option('colheader_justify', 'left')    显示的单元格内容靠左边还是右边

# DataFrame 类

DataFrame 类设计用来管理具有索引和标签的数据
会自动生成的一列的索引，从0开始，列名为标签。

## 创立

```python
#创建，行列标签默认都为可选缺省值np.arrange(n)，copy是复制数据
pandas.DataFrame( data, index, columns, dtype, copy)
# 例子
df = pd.DataFrame([10,20,30,40].columns=['numbers'],index=['a','b','c','d'])

# 创建空的DataFrame
pd.DataFrame()
```


可以从列表、字典、Series、Numpy ndarrays、另一个DataFrame中创建DataFrame

- 列表 

从单个列表，会自动生成索引
用列表嵌套的方式进行生成

```python
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],index=["2","3","4"],dtype=float)
print(df)

```


- ndarrays/Lists的字典

以键作为列名，以值作为元素，自动生成（可以指定）索引

```python
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

```


- 字典的列表

是以每个字典为行的方式进行的加载，字典的键为列，没有的键会形成新的列，若指定了columns，那么只会显示有的列

```python
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print(df1)

```


- 从Series的字典

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df
```


![image-20201022134757098](Learnpd.assets/image-20201022134757098.png)

## 获取各种属性

```python
dfname._stat_axis.values.tolist() # 行名称
dfname.columns.values.tolist()    # 列名称

df[i].value_counts()
```


## 编辑

https://www.yiibai.com/pandas/python_pandas_dataframe.html

```bash
train['工作饱和度'] = saturation_str   # 增加一列
train.insert(4, '工作饱和度', saturation_str)   # 插入一列
```


df.append()是创建了一个新的对象

索引

处理缺漏

# Series类

## 创建

Series类型由一组数据及与之相关的数据索引组成

## 基本操作

可以用自动索引或者index值都可以进行读取

##### 添加列

```python
df.loc[0]=['cat', 3]  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
# 也可采用诸如df.loc['a'] = ['123',30]的形式
```


添加一个空的列

mydf['列名'] = None

## 性质



运算中会自动对齐不同索引的数据

可以随时修改并能即刻生效

# 数据的透视

对数据的连接处理

con

# 排序与取值

## 取值与切片操作

```python
df['x']      取列名为'x'的列,格式为series
df[['x']]    取列名为'x'的列，格式为Dataframe
df[['w','z']]    取多列时需要用Dataframe的格式
df[df.columns[0:3]]    按照索引位置来取列，其实是分两步，先用索引取列名，再用列名取列
```


loc['A']取名为‘A’的行

iloc 含下界，不含上界 返回值是一个序列

```php
df.iloc[1,1]    根据绝对索引来取值，所谓绝对索引即按照0，1，2这样的人眼顺序来进行排列的原始索引  
df.iloc[0:3, [0,1]]
df.iloc[1]   绝对索引第一行
```


# 读取于存储csv文件
