# torch

a = torch.randn(1,2,3,4) 生成该形状的数组
a.size() a.transpose() 

# torch.nn

## 容器

### 模块

模型是类Model的实例化，而Mode继承于nn.Modole

```python
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
# 层的定义

    def forward(self, x):
#前向传递的定义
```

add_module( name,module)
apply(*fn*)
bfloat16()
buffers(*recurse=True*)

eval() 变为评估模式等价于self.train(False)

### Sequential

也是容器的一种，更加结构化

两种表达方式：

```python
  model = nn.Sequential(
                  nn.Conv2d(1,20,5),
                  nn.ReLU(),
                  nn.Conv2d(20,64,5),
                  nn.ReLU()
                )
#通过字典的方法
model = nn.Sequential(OrderedDict([
                  ('conv1', nn.Conv2d(1,20,5)),
                  ('relu1', nn.ReLU()),
                  ('conv2', nn.Conv2d(20,64,5)),
                  ('relu2', nn.ReLU())
                ]))

```



## nn.Identify

占位参数

## nn.linear

```
torch.nn.Linear(in,out,bias = True)
# in:(N,*,H_in)
# out(N,*,H_out)

```



卷积层
池化层
填充
Non-linear activations (weighted sum, nonlinearity)
Non-linear activations (other)
归一化层
Recurrent layers
Transformer layers
线性层
Dropout layers
Sparse layers
Distance functions
Loss functions
Vision layers
DataParallel layers (multi-GPU, distributed)
Utilities
Quantized Functions