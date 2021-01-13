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
## 最简单的版本
**需要满足的功能：**

- Dataset 提供整个数据集的随机访问功能，每次调用都返回单个对象，例如一张图片和对应 target 等等
- Sampler 提供整个数据集随机访问的索引列表，每次调用都返回所有列表中的单个索引，常用子类是 SequentialSampler 用于提供顺序输出的索引 和 RandomSampler 用于提供随机输出的索引
- BatchSampler 内部调用 Sampler 实例，输出指定 batch_size 个索引，然后将索引作用于 Dataset 上从而输出 batch_size 个数据对象，例如 batch 张图片和 batch 个 target
- collate_fn 用于将 batch 个数据对象在 batch 维度进行聚合，生成 (b,...) 格式的数据输出，如果待聚合对象是 numpy，则会自动转化为 tensor，此时就可以输入到网络中了
