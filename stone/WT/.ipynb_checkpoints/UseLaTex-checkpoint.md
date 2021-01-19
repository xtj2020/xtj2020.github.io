latex模块

# 章节

\section
\subsection
\subsubsection

# 使用图片

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.5\textwidth]{donate.jpg}
  \caption{一键三连求赞}
\end{figure}

# 不缩进 加粗
\noindent  \textbf{赞赏费用的使用解释权归 Elegant\LaTeX{} 所有，并且不接受监督，请自愿理性打赏}。

# 内置文字类型
\lstinline{founder} 

# 进行枚举（带编号）

\begin{enumerate}

\item

\end{enumerate}

# 链接
\href{https://github.com/peggy2006xzyz}{YPY}

# 不带编号进行枚举

\begin{itemize}
 \item

\end{itemize}


# 使用代码块
\begin{lstlisting}
\author{author 1\\ org. 1 \and author 2 \\ org. 2 }
\end{lstlisting}


# 使用Latex公式
\begin{equation}
  \int_{R^q} f(x,y) dy.\emph{of\kern0pt f}
\end{equation}




<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], inlineMath: [['$','$']] } }); </script>

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


```python
使用JS插件
<script src="ut.js" type="text/javascript"></script>

使用公式渲染
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

代码展示
https://nbviewer.jupyter.org/urls/xtj2020.top/toolbox/aa.ipynb
```
