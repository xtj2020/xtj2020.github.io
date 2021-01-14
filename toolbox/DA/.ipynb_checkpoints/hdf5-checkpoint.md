# 使用pickle

```python
import pickle

with open('staytim_li.pkl', 'wb') as f:
    pickle.dump(staytim_li, f)
        
pkl_file = open('staytim_li.pkl', 'rb')
data1 = pickle.load(pkl_file)
```


# h5py

<https://www.jianshu.com/p/998c861d32e3>

## 创建

h5file = h5py.File(filename,'w')

```python
X = h5file.create_dataset(shape=(0,args.patch_size,args.patch_size),　    #数据集的维度
maxshape = (None,args.patch_size,args.patch_size),     #数据集的允许最大维度　
dtype=float,compression='gzip',name='train',                      #数据类型、是否压缩，以及数据集的名字
                              chunks=(args.chunk_size,args.patch_size,args.patch_size))         #分块存储，每一分块的大小
```


## 以np为基础的HDF5操作



## 以pd为基础的HDF5操作
<https://www.cnblogs.com/feffery/p/11135082.html>

### 写出

**主要参数：** \
　path：字符型输入，用于指定h5文件的名称（不在当前工作目录时需要带上完整路径信息）

　　mode：用于指定IO操作的模式，与Python内建的open()中的参数一致，默认为'a'，即当指定文件已存在时不影响原有数据写入，指定文件不存在时则新建文件；'r'，只读模式；'w'，创建新文件（会覆盖同名旧文件）；'r+'，与'a'作用相似，但要求文件必须已经存在；

　　complevel：int型，用于控制h5文件的压缩水平，取值范围在0-9之间，越大则文件的压缩程度越大，占用的空间越小，但相对应的在读取文件时需要付出更多解压缩的时间成本，默认为0，代表不压缩
  
**创建：** \
一个HDF5 IO对象store：
```python
import pandas as pd
store = pd.HDFStore('demo.h5')
'''查看store类型'''
print(store)
```

**数据的写入：**
　第一种方式利用键值对将不同的数据存入store对象中，这里为了代码简洁使用了元组赋值法：
```python
store['s'],store['df'] = s,df
```
　　第二种方式利用store对象的put()方法，其主要参数如下：

　　key：指定h5文件中待写入数据的key

　　value：指定与key对应的待写入的数据

　　format：字符型输入，用于指定写出的模式，'fixed'对应的模式速度快，但是不支持追加也不支持检索；'table'对应的模式以表格的模式写出，速度稍慢，但是支持直接通过store对象进行追加和表格查询操作

　　使用put()方法将数据存入store对象中：

 
```python
store.put(key='s',value=s);store.put(key='df',value=df)
```
**查看属性：** \
store.items store对象只有items和keys属性，没有values属性 \
store['df'] 调用store对象中的数据直接用对应的键名来索引即可

**删除：**
一、是使用remove()方法，传入要删除数据对应的键：
```python
store.remove('s')
print(store.keys())
```
二、是使用Python中的关键词del来删除指定数据：
```python
del store['s']
print(store.keys())
```
**持久化到本地:**
```python
store.close()
##　查看store连接状况，False则代表已关闭
store.is_open

#导出到已存在的h5文件中，这里需要指定key
df_.to_hdf(path_or_buf='demo.h5',key='df_')
#创建于本地demo.h5进行IO连接的store对象
store = pd.HDFStore('demo.h5')
```
**读入:**
```python
# 第一种
store = pd.HDFStore('demo.h5')
'''方式1'''
df1 = store['df']
'''方式2'''
df2 = store.get('df')
df1 == df2


# 第二种
print(store.is_open)
df = pd.read_hdf('demo.h5',key='df')

# 关闭后的再次提取
store.close()
print(store.is_open)
df = pd.read_hdf('demo.h5',key='df')
df
```
