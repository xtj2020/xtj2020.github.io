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

