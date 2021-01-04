# 目标
对比赛数据进行初步的分析,分析难点在于有多种类型的数据，每种类型又有三种不同的像素、尺寸，以及对应的0、1标签。

- [ ] 用柱状图对数据进行合适的描述
- [ ] 用饼状图来表示数据的分布

## catplot() 分类图

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
