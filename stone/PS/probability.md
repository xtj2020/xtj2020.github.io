<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], inlineMath: [['$','$']] } }); </script>

# 题目
1、假设只考虑天气的两种情况：有雨或无雨，若已知今天的天气情况，明天天气保持不变的概率为p，变的概率为1-p，设第一天无雨，试求第n天也无雨的概率。

2、甲、乙比赛射击，每进行一次，胜者得1分，在一次射击中，甲胜的概率为$\alpha$,乙胜的概率为$\beta$,设$\alpha > \beta$,$\alpha + \beta =1$，且独立进行比赛到有人超过对方2分就停止，多得两分者胜。求甲、乙获胜的概率。

3、设随机变量X与Y独立同分布，其密度函数为$f(x) = \begin{cases}e^{-x},x>0 \\ 0, x \le 0 \end{cases}$  \
1).设U = X+Y与$V = {X \over X+Y}$的联合概率密度$f(u,v)$； \
2).判断U和V是否独立；

4、设二维随机变量（X,Y）的密度概率为$f(x,y) = {8 \over 3},0 \le x-y \le 0.5,0 \le x \le 1 ,0 \le y \le 1$,求:  \
1).X的边沿密度函数；  \
2).$P(x < {1 \over 2} \vert Y = {1 \over 2})$； \
3).(X,Y)的相关系数$r_{X,Y}$；

5、设随机变量X仅在[a,b]上取值，方差存在，试证：$a \le E(x) \le b,D(x) \le ({b-a \over 2})^2$

6、设离散型随机变量X的分布律为：$P(X = -1)=P(X=1)={1 \over 4},P(X=0)={1\over2},令Y=X^2$，求： \
1).Y的方差D（Y）； \
2).$(X,Y)$的联合分布列； \
3).$(X,Y)$的协方差Cov(X,Y)；

7、设X为随机变量，若$E(e^{ax})<\infty(a>0) $,证明：$P(X \ge x)\le e^{-ax} E(e^{aX}) $

8、设${X_n,n \ge 1}$为独立的随机变量序列，其分布为：$P(X_k = \sqrt k) = P(X_k = -\sqrt k) = {1 \over 2},k =1,2,3,...,$试证${X_n,n \ge 1}$服从中心极限定理

# 复习重点
总共七道题，完整做出两道及格，有一道完全陌生的题。

## 第一章 随机事件和概率
**知识点：** 求概率的基础题，带级数带极限的概率题，全概率公式

**书本题：** p63页 串并联 p76 例2.1.7、例2.1.8 课后题55、56、58、59、60、 64、66

**课上题：**

- 甲盒中有n_1个白球，n_2个红球，乙盒中有m_1个白球，m_2个红球。从甲盒中抽一个球放入乙盒中，再从乙盒中取一个球，求该球为红色的概率？

- 设在一个家庭中有n个小孩的概率为$p_n = \begin{cases} \alpha p^n, & n \ge1 \\ 1-{\alpha \over 1-p},& n=0\end{cases}$,$0 < \alpha < {1-p \over p},0<p<1 $，若生男生女是等可能的，求恰好有k个男生的概率。

- $\xi$是$(\Omega,\mathcal{F},P)$上的随机变量，$\mathcal{B}$是R上的Bovel $\sigma$代数。$\forall B \in \mathcal{B}$,令$F(B) = P(w;\xi(w)\in B),证明（R，\mathcal{B}，\mathcal{F}）$是一个概率空间。P30

## 第二章 随机变量及其分布函数
**知识点：**

三种问题
$F(x,y) ..... \longrightarrow F_x(x)$
$p(i,j) \longrightarrow p_{i,} = p{x=x_i}$
$f(x,y) \longrightarrow f_x(x)$

几种分布（会下面类型的就可以了）
1、$x \sim t(n)$，则${1 \over x^2} \sim \underline{ F(n,1)}$

2、$x \sim F(n,n),则P(x>1) = \underline{1 \over 2}$

多维随机变量有两道大题，共30分

随机变量的函数及其分布函数，两道大题。（和的分布可能会考）

定理2.4.7

**书本题：** p181 20、29、30、31、35

**课上题：**

- 从1...6中任意取一个数X，从1...X中取Y，求Y的分布列。

- 设$a \subset \Omega$,令$I_A(w) = \begin{cases} 1 ,&w \in A \\\\ 0 ,& w \notin A\end{cases}$，证明$I_A$为随机变量

- $X \sim U(-a,a),Y \sim U(-a,a)$相互独立，求Z=X+Y的密度 (1)、注意上下限的问题 (2)、$F^{(z)}_z = p(x+y < z)$

- $(\Omega,\mathcal{F},P)，A、B \in \mathcal{F},X = \begin{cases} 0 & w \in \bar A \\\\ 1 &w \in A\end{cases},  y = \begin{cases} 0 & w \in \bar B \\\\ 1 &w \in B\end{cases}$   (1)、若X、Y独立，$\forall x,y \in R,p{X <x.Y<y} = p(x<X)p(y<Y)$   (2)、若A、B独立

- $x \sim e^{\lambda_{(1)}},y \sim e^{\lambda_{(2)}}$独立，则Z=min(x,y)的密度函数

- 设$\xi$的密度函数为$f^{(x)}_\xi=\lambda^2xe^{-\lambda x},x \ge0,\lambda >0,令y \sim U(0,\xi)$,求P(y>2)

- x取非负整数值，EX存在的，证：$EX=\sum\limits^{+\infty}_{n=1}P(x \ge n)$



## 第三章 随机变量的数字特征

**说明：**只考一题 $p_{xy}$

**课上题：**
- $ x_1 \rightarrow A - X , 1 - x_1 \rightarrow Y , E(X)=1,D(X)=0.1, E(Y)=2 ,D(Y)=3 ,p_{xy} = -0.5. \\ Z=X_1X+(1-X_1)Y$ 当$x_1$为何值时，该投资风险最小？

## 第四章 不考

## 第五章 极限定理
**知识点：** 依概率收敛、大数定理、切比雪夫不等式、辛钦大数定律、马尔可夫大数定律证明与应用

**说明：**
两三道大题，不考中心极限，只考大数定理与依概率收敛

**书上题：**
1、2、5、8

**课上题：**
- $（\xi ，n \ge 0)$独立同分布，$E \xi = u < +\infty,D \xi  = \sigma^2 < +\infty$,证明： $ S_n^2 = {1 \over n} \sum\limits^n_{n=1}(\xi_i-\bar \xi_n) ^2 \stackrel{p} \rightarrow \sigma^2 $ , 其中 $ \bar \xi = {1 \over n} \sum\limits_{i=1}^n \xi_i $

- 独立同分布$P(\xi_n = {3^k \over k^2})={2 \over 3^k},k=1,2,... \text 判断 \xi  \text 是否服从大数定律$
