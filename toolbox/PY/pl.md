# 去除杂字符串

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

