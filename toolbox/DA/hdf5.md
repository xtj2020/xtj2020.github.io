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
