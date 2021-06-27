# 常数和特殊函数
```python
# 导入常数
from scipy import constant as C

from scipy import special as S
S.cbrt(8)
S.exp10
S.sindg(90)
```

# 线性代数运算
```python
# scipy.linalg模块提供标准线性代数运算
#.det()计算方阵的行列式、.inv（）计算方阵的逆
from scipy import linalg
import numpy as np 
arr = np.array([[1, 2], [3, 4]])
linalg.det(arr)
iarr = linalg.inv(arr) #若是矩阵不可逆，则会抛异常LinAlgError: singular matrix 
```

# 优化

```python
from scipy import optimize

```
标量函数的根 \
最小二乘法拟合 \
局部最优点
