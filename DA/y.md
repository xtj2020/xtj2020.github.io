# 001 随机

```python
import random
X = [1, 2, 3, 4, 5, 6]
y = [0, 1, 0, 0, 1, 1]
zipped_data = list(zip(X, y))  
# 将样本和标签一 一对应组合起来,并转换成list类型方便后续打乱操作
random.shuffle(zipped_data)  
# 使用random模块中的shuffle函数打乱列表，原地操作，没有返回值
new_zipped_data = list(map(list, zip(*zipped_data)))  
# zip(*)反向解压，map()逐项转换类型，list()做最后转换
new_X, new_y = new_zipped_data[0], new_zipped_data[1]  
# 返回打乱后的新数据
print('X:',X,'\n','y:',y)
print('new_X:',new_X, '\n', 'new_y:',new_y)
```

