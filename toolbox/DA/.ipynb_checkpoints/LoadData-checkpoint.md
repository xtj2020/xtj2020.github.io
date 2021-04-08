读取图片的常用三种方法为matplotlib、PIL、openCV、openslide

# matplotlib

```python
#读取图片
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
cat = mpimg.imread('/home/xtu_conda/xtj2020/data/dogs-vs-cats/train/cat.1.jpg')
print(cat.shape) 
plt.imshow(cat) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
#将图片转为np数组




```


## 改变图片的尺寸

 img.resize((width, height),Image.ANTIALIAS)
 
 第二个参数：
Image.NEAREST ：低质量
Image.BILINEAR：双线性
Image.BICUBIC ：三次样条插值
Image.ANTIALIAS：高质量

# PIL

```python

from PIL import Image 

img = Image.open(file_path) #读入的是一个Image对象
imgSize = img.size  #大小/尺寸
w = img.width       #图片的宽
h = img.height      #图片的高
f = img.format      #图像格式
img.save(" ") #对图像进行保存

 ```

# openCV

```python
 import cv2
 img = img * 255 #有时候需要将图片进行转化   
 img = cv2.imread(file_path)  #读取图片信息,返回的是一个array

 #sp = img.shape[0:2]     #截取长宽啊
 sp = img.shape # [高|宽|像素值由三种原色构成]

# 可以对Image对象进行转化为ndarray对象

 ```
 
 
# 将数组转为图片

对图片的展示
plt.imshow(a)
plt.show()

对图片的存储
```python
import cv2
result_BGR = cv2.cvtColor(a*255, cv2.COLOR_RGB2BGR)
cv2.imwrite("/app/xtj/2.png", result_BGR)
```


# 目录操作

os.mkdir('')创建目录

os.rmdir('')移除目录

os.listdir('')列出目录内容（文件和文件夹）

os.chdir('')从当前目录跳转

glob('')会使用Unix shell的规则，而不是正则表达式
\*匹配任意名称 ？一个字符 [abc]一类 [!abc]非

```python
import glob
glob.glob('m*')
```


os.path.jion( )合并路径

s.startswith(" ")用来返回特定字符开头的布尔值

os.isdir与os.isfile判断是否为文件和目录



# 文件操作

## 打开

open() 可以用来打开或创建文件,是自带函数。r读 w写 x在文件不存在下创建并写 a 如果文件存在，在末尾追写。第二个字母t代表文本类型，b代表二进制文件。
open('create.txt','wt')

## 写

write()

print( )

## 读



exists()
os.path.exists()检查目录或文件是否存在

isfile()
os.path.isfile()检查是否为一个文件
.表示当前目录 ..表示上层目录

copy()复制到一个文件，shutil.move会移动一个文件
import shutil
shutil('create.txt','ohno.txt')

rename()
os.rename()

link()

symlink()

chmod()

chown()

abspath()

realpath()

remove()

# 代码基准

## 如何对文件进行改名

```python
import os 
import re
mylist = r"E:\下载\1"
mylist_list = os.listdir(mylist)
name_list = [ ]
for i in mylist_list:
    myobj = re.findall(r"[0-8][0-9]",i)
    mypath = os.path.join(mylist,i)
    mypath_2 = os.path.join(mylist,myobj[0])
    mypath_2 = mypath_2 + '.mp4'
    print(mypath_2)
    os.rename(mypath,mypath_2)	
    
import re
new_path = list()
mypath = r'G:\Mirror\Developed\哲学\新建文件夹'
old_name_list = os.listdir(mypath)
for i in old_name_list:
    old_path = os.path.join(mypath,i)
    new_i = re.sub(r'p[0-0]',"",i)
    new_path = os.path.join(mypath,new_i)
    os.rename(old_path,new_path)
print(os.listdir(mypath))
```


## md2anki

```python
#输入参数：第一个是md文件，第二个是生成的文件名
print("开始转换MarkDown文件为Key-Value文件")
print("设置分隔符为：@")
 
import sys
file_name=sys.argv[1]
output_file=open(sys.argv[2], "w+",encoding='UTF-8')
file=open(file_name, 'r', encoding='UTF-8')
 
for line in file:
	if line.startswith("##"):
		output_file.write('\n')
		output_file.write(line.strip("##").rstrip().lstrip()+'@')
	else:
		output_file.write(line.rstrip().lstrip() + " ")
 
 
output_file.close()
file.close()
```


# 去除文本中杂字符串

```python
with open('book.md',encoding='utf-8') as f:
    lines = f.readlines()
print(lines)
f.close()

lines2 = []
for line in lines:
    line = line.replace('·','')
    line = line.replace(':','')
    line = line.replace('：','')
    line = line.replace('．','')
    line = line.replace('\n','')
    line = line.replace(',','')
    line = line.replace(r'\'','')
    lines2.append(line) 

str_lines2 = ''
for line in lines2:
    str_lines2 += line

with open('book.md','w',encoding='utf-8') as f:
    f.write(str_lines2)
f.close()
```


```python
import os
import re
import time
 
 
def modify_md_content(top):
    for root, dirs, files in os.walk(top, topdown=False):
        # 循环文件
        for file_name in files:
            file_name_split = file_name.split('.')
 
            try:
                if file_name_split[-1] == 'md':
                    # 找到md文件并且复制一份md文件路径
                    md_file_path = os.path.join(root, '.'.join(file_name_split))
                    copy_md_file_path = os.path.join(root, '.'.join([f'{file_name_split[0]}_copy', file_name_split[1]]))
 
                    # 打开md文件然后进行替换
                    with open(md_file_path, 'r', encoding='utf8') as fr, \
                            open(copy_md_file_path, 'w', encoding='utf8') as fw:
                        data = fr.read()
                        # data = re.sub('\(/配图/', '(配图/', data)
                        # data = re.sub('<br>', '<br>\n', data)
                        # data = re.sub('<br>', '', data)
                        data = re.sub('^ #.*? ', '', data)
 
                        fw.write(data)  # 新文件一次性写入原文件内容
                        # fw.flush()
 
                    # 删除原文件
                    os.remove(md_file_path)
                    # 重命名新文件名为原文件名
                    os.rename(copy_md_file_path, md_file_path)
                    print(f'{md_file_path} done...')
                    time.sleep(0.5)
            except FileNotFoundError as e:
                print(e)
        time.sleep(0.5)
 
 
if __name__ == '__main__':
    top = r'/Users/mac/Desktop/'
    modify_md_content(top)
```


# 数文件夹

```
import os
import re
name_path = r"I:\data1\[HCC MVI- Moderately] TANG_GUI_LIU_0005043760_1"
file_list = os.listdir(name_path)
disease_name = [r"NonContrast1.0",r"NonContrast5.0",r"ArterialPhase1.0",r"ArterialPhase5.0",r"VenousPhase1.0",r"VenousPhase5.0",r"DelayPhase1.0",r"DelayPhase5.0"]
for j in range(len(file_list)):
    for i in range(len(find_name)):
        a = re.findall(find_name[i],file_list[j])
        if len(a) != 0:
            sub_path = os.path.join(name_path,file_list[j])
            print(sub_path)
            print(len(os.listdir(sub_path)))
```


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


## 文件操作

h5file = h5py.File(filename,'w')

w 覆盖创建新文件 \
r 只读 \
r+ 读写，要求文件必须存在
a 打开读写文件（如果文件不存在则创建） \
w- 这将创建一个新文件，但如果已经存在相同名称的文件，则会失败。

### 打开

```python
with h5py.File("name.hdf5", "w") as f:
    print f["missing_dataset"]
# core在内存中进行操作，backing_store    
f = h5py.File("name.hdf5", driver="core", backing_store=True)
```


### 数据类型

查看数据类型

dset.dtype \
dset.shape

可以用列表切片的方法进行读取

## Datasets

### 创建

```python
X = h5file.create_dataset(shape=(0,args.patch_size,args.patch_size),　    #数据集的维度
maxshape = (None,args.patch_size,args.patch_size),     #数据集的允许最大维度　
     dtype=float,compression='gzip',name='train',                      #数据类型、是否压缩，以及数据集的名字
     chunks=(args.chunk_size,args.patch_size,args.patch_size))         #分块存储，每一分块的大小
```


也可以使用字典的方式进行创建




## 以pd为基础的HDF5操作
<https://www.cnblogs.com/feffery/p/11135082.html>

### 写出
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


**追加行、列：** \
<https://cloud.tencent.com/developer/ask/189318>
<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_hdf.html>
