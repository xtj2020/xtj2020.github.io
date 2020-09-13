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

