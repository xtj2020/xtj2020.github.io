## 梯度

平常的一元（单变量）函数的导数是标量值函数，而多元函数的梯度是向量值函数。多元可微函数在点上的梯度，是以在上的偏导数为分量的向量[2]。

## 函数的优化

什么是

## 凸集与凸函数

### 直线上的点

$$ \forall x,y \in R^n $$ ,if $$ z = \theta x +(1-\theta)y,0<\theta<1 $$,then $$\ x_1,x_2,z $$ in a line 

### 凸集

$$ \forall x,y \in c $$ ,if $$ 0\leqslant\theta\leqslant 1,\theta x +(1-\theta)y \in c $$的集合称为凸集

###  凸函数

$ f:R^n \to R \ domf \ 为凸集，且对于 \forall x,y \in domf，\forall \theta,0 \leq \theta \leq 1  $有：
$$
f(\theta x+(1-\theta)y)\leq\theta f(x) +(1-\theta)f(y)
$$

## 凸函数的性质

### 一阶条件

a、domf 为凸集
b、$ \forall x,y \in domf,f(y) \geq f(x)+ \triangledown f(x)^T (y-x) $

### 二阶条件

f的二阶偏导数为f的Hessian矩阵

$ x\in domf 有\triangledown^2f(x) \succeq 0$,对于R上的函数，可以简化为$f^n \geq 0$

### 三阶条件

$$ J(\theta) = \frac 1 2 \sum*_{i=1}^m (h_*\theta(x^{(i)})-y^{(i)})^2 $$
