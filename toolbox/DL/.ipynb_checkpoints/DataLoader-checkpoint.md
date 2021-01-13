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
 
 
