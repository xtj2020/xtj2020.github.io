pd有点类似于数据库

# 展示信息

```python
df.head(10)
df.info()
type(df[1])
df.dtypes

from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_timedelta64_dtype
is_string_dtype(df[1])

#排序
.sort_index()方法在指定轴上根据索引进行排序，默认升序
.sort_index(axis=0, ascending=True)
```


# DataFrame 类

DataFrame 类设计用来管理具有索引和标签的数据
会自动生成的一列的索引，从0开始，列名为标签。

## 创立

```python
#创建，行列标签默认都为可选缺省值np.arrange(n)，copy是复制数据
pandas.DataFrame( data, index, columns, dtype, copy)
# 例子
df = pd.DtaFrame([10,20,30,40].columns=['numbers'],index=['a','b','c','d'])
```


![image-20201022134757098](Learnpd.assets/image-20201022134757098.png)

## 获取各种属性

```python
dfname._stat_axis.values.tolist() # 行名称
dfname.columns.values.tolist()    # 列名称
dfname.account_values
```


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


**添加一个空的列**

mydf['列名'] = None

## 性质



运算中会自动对齐不同索引的数据

可以随时修改并能即刻生效

# 数据的透视

对数据的连接处理

con

# 取值

## 取列

```python
df['x']      取列名为'x'的列,格式为series
df[['x']]    取列名为'x'的列，格式为Dataframe
df[['w','z']]    取多列时需要用Dataframe的格式
df[df.columns[0:3]]    按照索引位置来取列，其实是分两步，先用索引取列名，再用列名取列
```


## 切片操作

loc['A']取名为‘A’的行

iloc 含下界，不含上界 返回值是一个序列

```php
df.iloc[1,1]    根据绝对索引来取值，所谓绝对索引即按照0，1，2这样的人眼顺序来进行排列的原始索引  
df.iloc[0:3, [0,1]]
df.iloc[1]   绝对索引第一行
```


# 获取信息

```python
df.index    行名称
df.columns  列名称
df._info_axis_     列名称

（bike1，bike2）=df.shape  行、列高度
len(df)    输出的是行高
df.index.size    行高
df.columns.size   列高
```


# 排序

# 多重索引

# 插入行、列

```bash
train['工作饱和度'] = saturation_str   # 增加一列
train.insert(4, '工作饱和度', saturation_str)   # 插入一列
```


# 计算

# 拼接与拆分

df.append()是创建了一个新的对象

# pd显示

pd.set_option('display.width', 200)   # 横向最多显示多少个字符， 一般80不适合横向的屏幕，平时多用200.pd.set_option('display.max_columns', 12)
 pd.set_option('display.max_rows', 10)  # 显示的最大行数和列数
pd.set_option('colheader_justify', 'left')    显示的单元格内容靠左边还是右边
