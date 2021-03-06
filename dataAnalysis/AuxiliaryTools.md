导入头文件

``` python
from tabulate import tabulate
import wcwidth
```


自定义格式

``` python
table_header = ['Name', 'Chinese', 'Math', 'English']
table_data = [
...     ('Tom', '90', '80', '85'),
...     ('Jim', '70', '90', '80'),
...     ('Lucy', '90', '70', '90'),
... ]

>>> print(tabulate(table_data, headers=table_header, tablefmt='grid'))
+--------+-----------+--------+-----------+
| Name   |   Chinese |   Math |   English |
+========+===========+========+===========+
| Tom    |        90 |     80 |        85 |
+--------+-----------+--------+-----------+
| Jim    |        70 |     90 |        80 |
+--------+-----------+--------+-----------+
| Lucy   |        90 |     70 |        90 |
+--------+-----------+--------+-----------+
```


简介
https://python.fasionchan.com/zh_CN/latest/libs/tabulate.html

官方文档
https://pypi.org/project/tabulate/

# tqdm

```python
from tqdm import notebook
tqdm_notebook(迭代器)
```


<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

# 使用PlotNeuralNet

运行

```
$ mkdir my_project
$ cd my_project
vim my_arch.py
bash ../tikzmake.sh my_arch
```


模版

```python
import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 512, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    to_connection( "pool1", "conv2"),
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    to_connection("pool2", "soft1"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
```


# TiddlyWiki
## 常用插件

Highlight
KaTeX
Core:TiddlyWiki5 core

## text/vnd.tiddlywiki
```wiki
# 增加空行
<br/><br/>
# 警告
<<.warning "Don't attempt to use the browser ''File''/''Save'' menu option to save changes (it doesn't work)">>
# 内嵌某个页面
{{}}

# 多标签转换
<<tabs "Forums Latest Tutorials [[Community Editions]] [[Community Plugins]] [[Community Themes]] [[Community Palettes]] [[Other Resources]] Examples Articles Meetups" "Latest">>

# contents中列表
list:[[]]

# 初始页面
Default tiddlers:

# 生成列表
Saving中的可以进行脚本的编写

# 复选框
<$checkbox tag="done"> Is it done?</$checkbox>

# 如何生成TableOfContents
新建TableOfContents块

子页中TableOfContents

```
