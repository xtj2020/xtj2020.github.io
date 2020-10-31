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

# 读取医学图片信息

模块的导入

```pythom
import os
import re
import pandas as pd
import numpy as np
```

函数的定义

```python

'''
定义的函数功能：
get_name(person_info)
get_type(person_info)
get_degreeed(person_info)
get_person_infoAndpath(main_path) 获取每个人的文件名与路径名
get_photo_conuts(person_path) 获取每个人每种疾病的文件数目
'''

#从主目录中获得子目录，根据子目录文件夹获得病人的病症、程度、姓名（姓名作为“主键”）
def get_name(person_info):
    matchRule_PersonName = re.compile("([A-Z]+_*){1,3}(?=_\d)")
    personName = re.search(matchRule_PersonName,person_info)
    if personName != None:
        person_name = personName.group()
        return person_name

def get_type(person_info):
    if '[肝血管瘤]' in person_info  or 'ANG' in person_info:
        disease_type = 'ANG'
    elif '[肝囊肿]'  in person_info or 'Cyst' in person_info:
        disease_type = 'Cyst'
    elif '[肝脏局灶性结节增生]'  in person_info  or 'FNH' in person_info:
        disease_type = 'FNH'
    elif '[肝细胞癌]'  in person_info  or 'HCC' in person_info:
        disease_type = 'HCC'
    elif '[转移瘤]'  in person_info  or 'Metastasis' in person_info:
        disease_type = 'Metastasis'
    elif '[正常肝脏]'  in person_info  or 'Normal' in person_info:
        disease_type = 'Normal'
    else:
        disease_type = 'other'
    return disease_type
        
def get_degreed(person_info):
    degreed_type =  ["Well","Moderately","Poorly"]
    for degreed in degreed_type:
        if degreed in person_info:
            person_degreed = degreed
    return person_degreed

# 主文件夹，病人信息文件夹（person_info,person_path）,照片文件夹(photo_info,photo_path)
#person_info获得每个人的信息
def get_person_infoAndpath(main_path):
    person_info = os.listdir(main_path)
#person_path是一个存储病人简历的一个列表文件
    person_path = []
    for i in person_info:
        path = os.path.join(main_path,i)
        person_path.append(path)
    return person_info,person_path

#需要获取的是病人每种切片的个数
def get_photo_conuts(person_path):
    photo_path =[]
    for photo_info in  os.listdir(person_path):
        photo_path.append(os.path.join(person_path,photo_info))
#    df_photo_counts = pd.DataFrame(columns=['NonContrast1.0','NonContrast5.0','VenousPhase1.0','VenousPhase5.0','ArterialPhase1.0','ArterialPhase5.0','DelayPhase1.0','DelayPhase5.0'])
#     df_photo_counts=pd.DataFrame()
    photos_counts=dict()
#子疾病的文件数目
    for i in range(len(photo_path)):
        if 'NonContrast1.0'  in photo_path[i]:
            photos_counts['NonContrast1.0'] = len(os.listdir(photo_path[i]))
        elif 'NonContrast5.0'  in photo_path[i]:
            photos_counts['NonContrast5.0'] = len(os.listdir(photo_path[i]))
        elif 'VenousPhase1.0'  in photo_path[i]:
            photos_counts['VenousPhase1.0'] = len(os.listdir(photo_path[i]))
        if 'VenousPhase5.0'  in photo_path[i]:
            photos_counts['VenousPhase5.0'] = len(os.listdir(photo_path[i]))    
        if 'ArterialPhase1.0'  in photo_path[i]:
            photos_counts['ArterialPhase1.0'] = len(os.listdir(photo_path[i]))
        if 'ArterialPhase5.0'  in photo_path[i]:
            photos_counts['ArterialPhase5.0'] = len(os.listdir(photo_path[i]))
        if 'DelayPhase1.0'  in photo_path[i]:
            photos_counts['DelayPhase1.0'] = len(os.listdir(photo_path[i]))
        if 'DelayPhase5.0'  in photo_path[i]:
            photos_counts['DelayPhase5.0'] = len(os.listdir(photo_path[i]))
#    nnew = pd.DataFrame(photos_counts,index=[1])
#     df_photo_counts = pd.concat([df_photo_counts,nnew],axis=0)
#     print(df_photo_counts)
    return photos_counts
```

主函数的运行

```python
main_path = "H:\肝脏局灶性病变分类原始图像6"
person_info,person_path = get_person_infoAndpath(main_path)
main_dict = dict()
df_main = pd.DataFrame()
for i in range(len(person_info)):
    main_dict["name"]=get_name(person_info[i])
    main_dict["type"]=get_type(person_info[i])
    main_dict["degreed"]=get_degreed(person_info[i])
    main_dict.update(get_photo_conuts(person_path[i]))
    df_dict = pd.DataFrame(main_dict,index=[i])
    df_main = pd.concat([df_main,df_dict],axis=0)
print(df_main)
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

