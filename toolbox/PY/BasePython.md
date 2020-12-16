# python基础
##### 内置函数

abs( ) 返回绝对值，是复数返回模

all( ) iterable对象均为真返回True

any( )

ascil( )



##### 实现扩充数据结构

##### 常见自带库

##### python中的迭代

python中的迭代通过for ...in...来实现，能用于所有可迭代对象

如何判断一个对象是可迭代对象：

```python
from collections import itreable
isintance('abc',iterable)
```


可以用enumerate将一个list变为索引元素对

```python
for i,value enumerate(['a','b','c']):
```


# 使用jupyter

## 进度条

```python
# 安装
pip install tqdm
conda install -c conda-forge tqdm
# trange()来代替tqdm(range()),可以使用desc来设置文字说明
# 预先实例化进度条对象，在需要刷新说明文字的时候执行相应的程序
bar = trange(10)
for i in bar:
	bar.set_description(f'第{i}轮')
# tqdm.notebook来美化jupyter
# 你可以将pandas中的任何apply操作替换为progress_apply，并且记住每个单独的progress_apply前要先执行tqdm.pandas()

```


# 对文件的操作

https://my.oschina.net/u/3018050/blog/1799044

```python
os.path.exists(path)
os.mkdir(path)
os.mkdirs(path)

file = open('C:\\Users\Administrator\\Desktop\\' + 'new' + '.txt','w')
file.close()

os.renames(src,dst)	#递归式的给文件或文件名改名
# 文件或文件夹的最后访问时间，从新纪元到访问时的秒数
os.getatime(path)
# 文件或文件夹的最后修改时间
os.getmtime(path)
# 文件或文件夹的创建时间
os.getctime(path)	

```
