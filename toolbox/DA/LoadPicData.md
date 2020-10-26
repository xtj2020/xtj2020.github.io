# 模块的导入

```pythom
import os
import re
import pandas as pd
import numpy as np
```

# 函数的定义

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

# 主函数的运行

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

