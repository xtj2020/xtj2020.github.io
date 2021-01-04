# 目标
对比赛数据进行初步的分析,分析难点在于有多种类型的数据，每种类型又有三种不同的像素、尺寸，以及对应的0、1标签。

- [ ] 用柱状图对数据进行合适的描述
- [ ] 用饼状图来表示数据的分布

## catplot() 分类图

http://seaborn.pydata.org/tutorial/categorical.html

https://cloud.tencent.com/developer/article/1506468

### 函数原型

``` python

seaborn.catplot(x=None, y=None, hue=None,
                data=None, row=None, col=None,
                col_wrap=None, estimator=<function mean>, ci=95, 
                n_boot=1000, units=None, order=None,
                hue_order=None, row_order=None, col_order=None, 
                kind='strip', height=5, aspect=1, orient=None, 
                color=None, palette=None, legend=True,
                legend_out=True, sharex=True, sharey=True, 
                margin_titles=False, facet_kws=None, **kwargs)


```

### 使用
``` python

import seaborn as sns

``` 

必须的参数data 其他参数均为可选；

data:是DataFrame类型的;

x,y为数据中变量的名称(如上表，date,name,age,sex为数据字段变量名);

row，col：数据中变量的名称
作用：设置分类变量将决定网格的分面。

kind：字符串
要绘制的绘图类型
(对应于分类绘图功能的名称:"count"-统计图, "point"-点, 
"bar"-条形, "strip"-条形, "swarm"-群形, "box"-框形, 
"violin"-小提琴形, or"boxen"-盒形.）

col_wrap:int类型数值
作用：让每行显示指定数量的图，如果超过该数量，则多行显示。

orient:方向：v或者h
作用：设置图的绘制方向(垂直或水平)
如何选择：一般是根据输入变量的数据类型(dtype)推断出来。


### 艺术风格的设置

https://blog.csdn.net/ICERON/article/details/85088582

### 八种接口

catplot() 分类图(它是下面8种图的接口，下面八种图表均可通过指定kind参数来绘制)

1.stripplot() 分类散点图

2.swarmplot() 能够显示分布密度的分类散点图

3.boxplot() 箱图、盒形图

4.violinplot() 小提琴图

5.boxenplot() 增强箱图

6.pointplot() 点图

7.barplot() 条形图

8.countplot() 计数图


### 应用

https://www.jianshu.com/p/94931255aede

# 数据均衡

模型评价指标 https://blog.csdn.net/login_sonata/article/details/54288653

不均衡有两种情况：内在不均衡与外在不均衡。内在不均衡是总体本身就是不均衡的；外在不均衡是指总体是平衡的，但采样的原因导致不均衡。
对评价指标的理解 https://www.cnblogs.com/sddai/p/5696870.html

解决办法有：
- 扩充数据集
- 重新采样
- 人造数据
- 改变分类算法
    - 在代价函数中增加小样本的权重，减小大样本的权重
    - 
- 尝试其它评价指标
    - 混淆矩阵
    - 准确率
    - 精准率
    - 召回率
    - F1分数
    - AOC
    - DUA

```{.python .input  n=5}
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
#     fig = plt.figure(figsize=(10,6))
    for i in range(1,7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sinplot()
```

```{.json .output n=5}
[
 {
  "ename": "ModuleNotFoundError",
  "evalue": "No module named 'seaborn'",
  "output_type": "error",
  "traceback": [
   "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
   "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
   "\u001b[0;32m<ipython-input-5-86f38a229fa4>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mseaborn\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0msns\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyplot\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0msinplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mflip\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
   "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'seaborn'"
  ]
 }
]
```

```{.python .input  n=4}
sns.set(style='darkgrid',font_scale=1.5)

# 利用此方法可以快速设置seaborn的默认风格，当然也可以添加参数设置其他风格
# font_scale：float，单独的缩放因子可以独立缩放字体元素的大小。

sinplot()
```

```{.json .output n=4}
[
 {
  "ename": "NameError",
  "evalue": "name 'sns' is not defined",
  "output_type": "error",
  "traceback": [
   "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
   "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
   "\u001b[0;32m<ipython-input-4-f9a9a78533c0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0msns\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mset\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstyle\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'darkgrid'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mfont_scale\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1.5\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;31m# \u5229\u7528\u6b64\u65b9\u6cd5\u53ef\u4ee5\u5feb\u901f\u8bbe\u7f6eseaborn\u7684\u9ed8\u8ba4\u98ce\u683c\uff0c\u5f53\u7136\u4e5f\u53ef\u4ee5\u6dfb\u52a0\u53c2\u6570\u8bbe\u7f6e\u5176\u4ed6\u98ce\u683c\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# font_scale\uff1afloat\uff0c\u5355\u72ec\u7684\u7f29\u653e\u56e0\u5b50\u53ef\u4ee5\u72ec\u7acb\u7f29\u653e\u5b57\u4f53\u5143\u7d20\u7684\u5927\u5c0f\u3002\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
   "\u001b[0;31mNameError\u001b[0m: name 'sns' is not defined"
  ]
 }
]
```
