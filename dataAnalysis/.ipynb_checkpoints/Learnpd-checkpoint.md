# 展示与统计信息


df.head(10) &#8194; df.info()  &#8194; type(df[1])  &#8194; df.dtypes 

## 排序
.sort_index()方法在指定轴上根据索引进行排序，默认升序 \
.sort_index(axis=0, ascending=True)

df.index    行名称 \
df.columns  列名称 \
df._info_axis_     列名称 \
（bike1，bike2）=df.shape  行、列高度

len(df)    输出的是行高 \
df.index.size    行高 \
df.columns.size   列高



## pd显示

pd.set_option('display.width', 200) \
横向最多显示多少个字符， 一般80不适合横向的屏幕，平时多用
200.pd.set_option('display.max_columns', 12) \
 pd.set_option('display.max_rows', 10)  \
显示的最大行数和列数 \
pd.set_option('display.max_rows', None) \
将所有内容进行展示

pd.set_option('colheader_justify', 'left')    显示的单元格内容靠左边还是右边

# 基本操作

## DataFrame创建
DataFrame 类设计用来管理具有索引和标签的数据
会自动生成的一列的索引，从0开始，列名为标签。

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


```python
out:
    one  two
a  1.0    1
b  2.0    2
c  3.0    3
d  NaN    4
```


## Series 操作

pd.Series(数据，索引)

https://www.jianshu.com/p/0ea5f5041f3f

Series类型由一组数据及与之相关的数据索引组成

```python
pd.Series([2,3,4,5,6])
pd.Series([2,3,4,5,6], index=['a', 'b', 'c', 'd', 'e'])
# 可以存储不同的类型
# 创建时自定义索引会替换字典索引
d2 = {
    'name': '张三',
    'age': 18,
    'gander': True,
}

d = pd.Series(d2, index=['name', 'age', 'score'])


```


可以用自动索引或者index值都可以进行读取

```python
df.loc[0]=['cat', 3]  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
# 也可采用诸如df.loc['a'] = ['123',30]的形式
```


添加一个空的列

mydf['列名'] = None

运算中会自动对齐不同索引的数据

可以随时修改并能即刻生效

## 获取各种属性

```python
dfname._stat_axis.values.tolist() # 行名称
dfname.columns.values.tolist()    # 列名称

df[i].value_counts()

# 获取index，需要将其转为list
list(df.index)
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




### 删除行、列

df4=df1.drop(labels=['gender',"age"],axis=1) \
axis = 0 是按行操作，axis = 1是按列操作　\
DataFrame.index = [newName]，DataFrame.columns = [newName]





## 取值

```python
df['x']      #取列名为'x'的列,格式为series
df[['x']]    #取列名为'x'的列，格式为Dataframe
df[['w','z']]    #取多列时需要用Dataframe的格式
df[df.columns[0:3]]    #按照索引位置来取列，其实是分两步，先用索引取列名，再用列名取列
#不能用df1[1]来进行取值
```


loc['A']取名为‘A’的行

iloc 含下界，不含上界 返回值是一个序列

```php
df.iloc[1,1]    根据绝对索引来取值，所谓绝对索引即按照0，1，2这样的人眼顺序来进行排列的原始索引  
df.iloc[0:3, [0,1]]
df.iloc[1]   绝对索引第一行
```


### 利用条件与组合条件筛选
- 筛选单个值 \
df[df.A==100]
- 筛选出A列值在num列表的数据条 \
num = [100, 200, 300] \
df[df.A.isin(num)]     
- 找出df中A列值为100且B列值为‘a’的所有数据 \
df[(df.A==100)&(df.B=='a')]
- 找出df中A列值为100或B列值为‘b’的所有数据 \
df[(df.A==100)|(df.B=='b')]

### 排序

按列索引排序
df.sort_index(axis=1,ascending=True,inplace=True)
ascending为升序排序，inplace是修改数据

按值排序，输入是一个列表
unsorted_df.sort_values(by='col1')

sort_values()提供了从mergeesort，heapsort和quicksort中选择算法的一个配置。Mergesort是唯一稳定的算法。

## 计算
即按行求和
df_pt["总和"] =df_pt.apply(lambda x:x.sum(),axis =1)
dataf_test1['diff'].sum()  // diff为要求和的列


# 数据的透视

https://www.cnblogs.com/onemorepoint/p/8425300.html

pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],aggfunc=[np.mean,len])





# 读取于存储csv文件

df = pd.read_csv('movies.csv') \
添加 skiprows 参数可以直接跳过前面的行 \
df.to_csv('to_mivies.csv')

使用numpy进行运算会保留索引，在算数运算中会会自动对齐不同索引的数据。

利用isnull与notnull来检测缺失数据

Series对象本身及其索引都有一个name属性，可以通过赋值的方式就地修改

## DataFrame
DataFrame 生成基本的统计指标

**定义：** DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔值等）。
可以视为Series的一个字典（共用一个索引，那么列名就是Series名吗？）。

横向：两个表的堆叠 concat axis = 1
纵向：

主键合并:merge

重叠合并:combine_first

指定了列序列，则DataFrame的列就会按照指定顺序排列!

通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series

为不存在的列赋值会创建出一个新列。关键字del用于删除列

嵌套字典来转换为DataFrame

切片或布尔型数组选取行

### 索引对象

pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等）。构建Series或DataFrame时，所用到的任何数组或其他序列的标签都会被转换成一个Index

Index对象是不可修改的（immutable)

drop方法返回的是一个在指定轴上删除了指定值的新对象


当使用非整数作为切片索引时,其末端是包含的（inclusive)
