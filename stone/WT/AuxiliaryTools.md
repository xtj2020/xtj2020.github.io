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

