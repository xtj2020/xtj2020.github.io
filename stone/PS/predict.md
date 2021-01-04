<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

# 预测算法

- 时间序列
- 神经网络预测
- 机理模型：微分方程
- 灰色预测

## 灰色预测

灰色模型

GM(1,1)模型
一阶线性微分方程
要求：
- 数据量不少于四个
- 数据非负，符合指数变化且变化规律不大
步骤：
- 数据预处理
    - 数据累加（使数据光滑,模型要有一阶可导性）
    - 紧邻近均值加权
    - 
    
- 灰色及白化微分方程系数的确定
    - 灰导数的定义
    - 灰微分方程模型
    - 确定系数（超定方程的求解）
- 数据还原及预测
    - 
    
### 灰色Verhulst模型

数据具有一定的饱和性，S形过程
- 

### 扩展
- Logistic
- SI模型

$\large {di \over dt }= \lambda i(t)(1-i(t))$


## 灰色波形预测

序列X的k段折线图形

$X={x_k = x(k) +(t-k)[x(k+1)-x(k)],x= }$

无效数据的剔除m
