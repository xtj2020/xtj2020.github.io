要有\_\_iter\_\_才能叫可迭代对象(iterable)
```python
from collections.abc import Iterable, Iterator
print(isinstance(cls_a, Iterable))

```
可迭代器(Iterator)一定是可迭代的，反之不一定成立
实现了 \_\_next\_\_ 和 \_\_iter\_\_ 方法的类才能称为迭代器，就可以被 for 遍历了。
