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
在代价函数中增加小样本的权重，减小大样本的权重

- 尝试其它评价指标
混淆矩阵
准确率
精准率
召回率
F1分数
AOC
DUA


# 异常数据的处理

## 异常数据的判断

常用的两种：物理方法和统计方法

### $3\sigma$准则

1. 计算均值$\bar x = \sum\limits_{i=1}^{n} x_i$
2. 计算标准差 $\sigma= \sqrt{ \ {1 \over n-1} \sum \limits_{i=1}^n(x_i - \bar x)^2}$
3. 小于$\bar x -3 \sigma$或者大于$\bar x +3 \sigma$的为异常值

### 肖维勒准则

1. 计算数据的$\bar x  \text 与 \sigma$；
2. 计算每个数据的的误差$e_i = \vert x_i - x \vert $
3. 查概率积分表得到$\varepsilon = w_n \sigma$
4. 若$e_i > \varepsilon $则为误差值

### t检验
1. 将数据从小到大排列，计算排除min得到均值与方差。
2. 查表得k(n,$\alpha$)
3. 检验最小值，计算$\vert x_{(1)} - \bar x\vert > k(n,\alpha)$是否成立,成立最小值为误差值，不成立，检验最大值

### 格拉布斯准则
1. 将数据从小到大进行排序
2. 求出数据的$\bar x \text 与\sigma$
3. 查表得$\lambda(n,\alpha)$
4. 异常数据小于$\bar x - \lambda \sigma \text 大于 \bar x + \lambda \sigma$

### 狄克逊准则

1. 样本从大到小进行排序
2. 根据$n, \text 和\alpha$查找系数$D(n,\alpha)$，计算低端统计量$r^,$与高端统计量r
3. 统计量$r>r'$且$r > D(n,\alpha),x_{(n)}$为异常值 \
$r < r'$且$r > D(n,\alpha),x_{(1)}$为异常值

### 箱体图

异常值的范围为$(0,Q_1-1.5IQR) (Q_2+1.5IQR,+ \infty)$

## 异常数据的处理

### 删除带有缺失值的样本或特征

**删除样本:** 多个特征存在缺失值，且缺失值占整个数据集比例不高 \
**删除特征:** 某个特征值缺失值较多且对数据分析的目标影响不大

data.Dropna()

### 填补（均值填补、随机填补和基于模型的填补）
pandas.DataFrame.fillna()

均值填补：连续的用平均值，离散的用众数

正态分布-均值、偏态分布-中位数、 有离群点的分布-中位数、名义变量-众数


在均值填补的基础加上随机项（贝叶斯与近似贝叶斯）

基于模型的填补：将缺失值作为预测目标。与数据有比较好的关联性，需要进行数据检验

### 插值法

拉格朗日插值法

### 不处理缺失值
