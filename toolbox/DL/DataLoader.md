## 可迭代对象
要有\_\_iter\_\_才能叫可迭代对象(iterable)

```python
from collections.abc import Iterable, Iterator
print(isinstance(cls_a, Iterable))

```


## 迭代器
可迭代器(Iterator)一定是可迭代的，反之不一定成立

实现了 \_\_next\_\_ 和 \_\_iter\_\_ 方法的类才能称为迭代器，就可以被 for 遍历了。

为什么list是可迭代对象，不是迭代器，但是能够进行迭代？
 
 list 内部的 \_\_iter\_\_ 方法内部返回了具备 \_\_next\_\_ 方法的类，或者说调用 iter() 后返回的对象本身就是一个迭代器，当然可以 for 循环了。
 
## getitem

## yield生成器

# DataLoader的实现

<https://zhuanlan.zhihu.com/p/340465632>

3分钟理解 pytorch 的 gather 和 scatter<https://zhuanlan.zhihu.com/p/319191164>

## 最简单的版本
**需要满足的功能：**

- Dataset 提供整个数据集的随机访问功能，每次调用都返回单个对象，例如一张图片和对应 target 等等
- Sampler 提供整个数据集随机访问的索引列表，每次调用都返回所有列表中的单个索引，常用子类是 SequentialSampler 用于提供顺序输出的索引 和 RandomSampler 用于提供随机输出的索引
- BatchSampler 内部调用 Sampler 实例，输出指定 batch_size 个索引，然后将索引作用于 Dataset 上从而输出 batch_size 个数据对象，例如 batch 张图片和 batch 个 target
- collate_fn 用于将 batch 个数据对象在 batch 维度进行聚合，生成 (b,...) 格式的数据输出，如果待聚合对象是 numpy，则会自动转化为 tensor，此时就可以输入到网络中了



# 自定义数据加载器

用Dataset封装自己的数据和标签
用DataLoader达到数据的划分

Dataset必须继承实现\_\_getitem\_\_、
\_\_len\_\_

```python
import torch
import numpy as np
# 定义GetLoader类，继承Dataset方法，并重写__getitem__()和__len__()方法
class GetLoader(torch.utils.data.Dataset):
	# 初始化函数，得到数据
    def __init__(self, data_root, data_label):
        self.data = data_root
        self.label = data_label
    # index是根据batchsize划分数据后得到的索引，最后将data和对应的labels进行一起返回
    def __getitem__(self, index):
        data = self.data[index]
        labels = self.label[index]
        return data, labels
    # 该函数返回数据大小长度，目的是DataLoader方便划分，如果不知道大小，DataLoader会一脸懵逼
    def __len__(self):
        return len(self.data)

# 随机生成数据，大小为10 * 20列
source_data = np.random.rand(10, 20)
# 随机生成标签，大小为10 * 1列
source_label = np.random.randint(0,2,(10, 1))
# 通过GetLoader将数据进行加载，返回Dataset对象，包含data和labels
torch_data = GetLoader(source_data, source_label)
```
