None
None
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], inlineMath: [['$','$']] } }); </script>


# 公式中的LaTex

- [上下标](./LaTex/上下标.html)-[edit](./LaTex/上下标.md)
- [关系符号](./LaTex/关系符号.html)-[edit](./LaTex/关系符号.md)
- [堆叠](./LaTex/堆叠.html)-[edit](./LaTex/堆叠.md)
- [字体](./LaTex/字体.html)-[edit](./LaTex/字体.md)
- [常规函数](./LaTex/常规函数.html)-[edit](./LaTex/常规函数.md)
- [特殊字符](./LaTex/特殊字符.html)-[edit](./LaTex/特殊字符.md)
- [界限](./LaTex/界限.html)-[edit](./LaTex/界限.md)
- [矩阵](./LaTex/矩阵.html)-[edit](./LaTex/矩阵.md)
- [空格破折号箭头](./LaTex/空格破折号箭头.html)-[edit](./LaTex/空格破折号箭头.md)

# 常用Latex公式

```
\begin{equation}
  \int_{R^q} f(x,y) dy.\emph{of\kern0pt f}
\end{equation}
```


\sigma $\sigma$

\sum\limits
 $\bar x = \sum\limits_{i=1}^{n} x_i$

 需要用 \vert 来替代 \|

 用\times 来替代* 用\div替代除法

\xi $\xi$ \delta $\delta$
\varepsilon $\varepsilon$
\lambda $\lambda$

\infty $\infty$

2 \stackrel{p} \rightarrow \delta^2  $2 \stackrel{p} \rightarrow \delta^2$



# 模板的使用

使用模板为eleantpaper

## 章节

```
\section
\subsection
\subsubsection
```


## 图片的使用

```

# 紧跟文字显示
\begin{figure}[H]
  \centering
  \includegraphics[width=1\textwidth]{XGOOST二分类.png}
\end{figure}

# 浮动显示
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.5\textwidth]{donate.jpg}
  \caption{一键三连求赞}
\end{figure}
```


## 新段落

不会按回车来设置新行和段落

```python
#新行
\newline
#强制最后一行覆盖整个页面宽度
\linebreak 
\\\
\\\\\ #会产生一个空白行
```


新段落
尽量使用预定义的宏来创建统一的段落

## 空格

一系列空格和Tab键产生的空格被视为一个

![img](https://xtj2020.top/webimg/LaTex/LaTex空格.png)





## 不缩进 加粗
\noindent  \textbf{赞赏费用的使用解释权归 Elegant\LaTeX{} 所有，并且不接受监督，请自愿理性打赏}。

## 内置文字类型
\lstinline{founder} 

## 进行枚举（带编号）

\begin{enumerate}

\item

\end{enumerate}

## 链接
\href{https://github.com/peggy2006xzyz}{YPY}

## 不带编号进行枚举

\begin{itemize}
 \item

\end{itemize}

``` python
三种方式来实现链接
This is an [example link](http://example.com/).

I get 10 times more traffic from [Google][1] than from [Yahoo][2] or [MSN][3].  

[1]: http://google.com/        "Google" 
[2]: http://search.yahoo.com/  "Yahoo Search" 
[3]: http://search.msn.com/    "MSN Search"

这是一个链接到谷歌的[^脚注]。

[^脚注]: http://www.google.com
```

