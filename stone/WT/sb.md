1. 关系图类：
   关注的是统计量之间的关系，比如x和y一般是数值型数据，关注两个数值变量之间的关系一般为散点图，曲线图等
2. 分类图
   通过分类之后关注统计量在类别上的分布，一般为散点图，箱图，小提琴图等
3. 分布图
   分布图表示的是变量取值时的概率大小的一种图形，一般有直方图，核函数密度估计图，双变量关系图等
4. 回归图
   描述线性关系的一种图形（将x和y的关系尽力用直线去拟合，有点像高中数学里面把散点用直线连起来 ）
5. 矩阵图
   研究是变量比较多（x比较多），把x两两组合查看之间的关系的一种图形，一般有热力图，聚集图等

https://www.cnblogs.com/biyoulin/p/9565350.html

查看linux下可用的中文字体
fc-list :lang=zh

``` python

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
``` 
防止字体重叠

https://www.jb51.net/article/191678.htm

柱状图
https://zhuanlan.zhihu.com/p/25128216
