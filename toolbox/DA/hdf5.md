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


##
