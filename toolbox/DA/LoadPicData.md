读取图片的常用三种方法为matplotlib、PIL、openCV、openslide

# matplotlib

```python
#读取图片
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
cat = mpimg.imread('/home/xtu_conda/xtj2020/data/dogs-vs-cats/train/cat.1.jpg')
print(cat.shape) 
plt.imshow(cat) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
#将图片转为np数组

```



# PIL