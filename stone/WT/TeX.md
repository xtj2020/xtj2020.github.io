## 长度

TeX中的长度
mm毫米
cm厘米
in英寸＝2.54cm＝72.27pt
pt点
em大写字母M的宽度
ex小写字母x的高度

弹性长度：根据需要自动伸缩
正常值plus伸展值minus收缩值
实际长度可超过正常值和伸展值之和，但不能小于正常值和收缩值之差

# 第一个例子

```tex
\documentclass[11pt]{article}%11pt字体，普通文章
%导言区，全局命令
\usepackage{CJK}%使用CJK宏包
\begin{document}%主环境
\begin{CJK}{GBK}{song}%汉字必须放入CJK环境
%其它字体:song,kai,fs,hei,li,you
%CJK的两种环境CJK和CJK*
%GBK是采用的字符集：GB，GBK，Bg5，Gbt
Hi,This is my first \LaTeX file
祝贺你，MikTex和CJK安装成功了
\end{CJK}
\ent{document}

CJK和CJK*环境之间的切换
\CJKspace和\CJKnospace


\CJKtilde 重新定义～的长度
```

## 基本约定

分组｛......｝
注释符：%
西文标点后要加空格
各种环境的开始和结束命令最好独占一行
换行:连续两个回车，一个仅为空格

## 输入特殊字符

前加\的有：#$%{}~_^&
\=\textbackslash
｜,<,>＝$|$,$<$,$>$,$*$(中间星）
*＝*上面星
特殊符号\s \p \dag \ddag \copyrigh版权号，\pounds 磅

\TeX \LaTeX \LaTeXe \AmS-\LaTeX(最后这个要amsmath宏包）

单引号：`'(1键前面的）
双引号：``"



 

## 西文字体属性、及中文字体属性、命令

字体有5种属性
族：
\rmfamily：罗马字体
\sffamily：无衬线字体
\ttfamily：打字机字体
形状：（shape）直立斜
\upshape：直立
\itshape：意大利斜体
\slshape：斜体
\scshape：小体大写
系列：（series）宽度黑度
\mdseries：中等权重（黑）
\bfseries：粗体

\normalfont：默认字体，中等权重直立罗马字体
西文尺寸：10pt，11pt，12pt
\em强调，一般为斜体
以上命令称为声明（无参数）

每一声明对应字体命令
命令只对其参数中的文本起作用
族：
\testrm{},\testsf{},\testtt{}
形状
\textup{},\textit{},\textsl{},\textsc{}
系列
\textmd{}，\textbf{}
默认值：\textnormal{}
强调：\emph{}

定义了基本尺寸后，可使用下面的声明来改变字体
\tiny  5pt
\scriptsize 7pt
\footnotesize 8pt
\small  9pt
\normalsize 10pt
\large  12pt
\Large  14.4pt
\LARGE  17.28pt
\huge  20.74pt
\Huge  24.88pt
以上尺寸是基本尺寸为10pt时的大小

所有西文字体命令对中文同样起作用
italic和slanted斜体对中文一样

中文书籍基本字号为5号约等于11pt

使用GBK编码时，可同时输入简繁体。

自定义字体大小
\fontsize{字体尺寸}{行距}后面须加上\selectfont才生效
可得到任意大小汉字，西文最大不能超\Huge
行距通常为字体大小的1.2-1.5倍
例：\fontsize{12pt}{\baselineskip}\selectfont
\usepackage{type1cm}任意大小西文

行距：\linespread{1.3}产生1.5倍行距，1.6产生双倍行距，效果夸张，不适合出版
用下面方法：\setlength{\baselineskip}{1.5\baselineskip}{......}

 

正文中更换字体：\CJKfamily{字体族}

为方便，作以下自定义
\newcommand*{\SONG}{\CJKfamily{song}}
\newcommand*{\HEI}{\CJKfamily{hei}}
\newcommand*{\KAI}{\CJKfamily{kai}}
\newcommand*{\FS}{\CJKfamily{fs}}
\newcommand*{\LI}{\CJKfamily{li}}
\newcommand*{\YOU}{\CJKfamily{YOU}}

引用更改为宋体：\SONG 正文

 

文本居中
文本默认为左对齐
单行文本居中命令
\centerline{....}
多行使用\begin{center}环境
居中声明：\centering（不建议使用）

## 参考文献环境

\begin{thebibliography}{编号样本}
\bibitem[记号]{引用标志} 文献条目
 .
 .
 .
\bibitem[记号]{引用标志} 文献条目
\end{thebibliography}

\bibitem[省略为方括号数字]{不可省由字母，数字和，号外符号组成，各个文献互不相
同} 文献条目
编号样本，指定记号的宽度，一般为数字

引用文献时用\cite{引用标志1，引用标志2}

调节各文献间距离
\setlength{\itemsep}{高度}

标题缺省为左对齐Reference
（\Large\bfseries）
由\refname值确定
书籍参考文献标题由\bibname值确定

文献条目包含：作者，标题，出版社，年代，版本，页码
一行放不下，后面自动缩进，距离为“编号样本”宽度

## 脚    注

\footnote{脚注内容}
article文档，整篇同一编号
book和report文档，每章统一编号

# 文档

```tex
\documentstyle[选项1,选项2,...]{article,book,report,letter,只能选一种}
```

article 短篇文章
report 长篇报告，可分章
book （书）可含chapter，奇偶页采用不同处理

可选项对整篇文档起作用，使用多个选项互不排斥，用逗号分隔
基本字体：10pt，11pt，12pt
纸张大小：letterpaper，a4paper，a5paper...
排版方向：portrait（竖向），landscape（横向）
标题页：titlepage，notitlepage，final和draft

指定纸张大小（只有latex2e中使用）
letterpaper（11*8.5in）
legalpaper（14*8.5in）
executivepaper（10.5*7.25in）
a4paper（29.7*21cm）
a5paper（21*14.8cm）
b5paper（25*17.6cm）
默认值是letterpaper，美国信纸尺寸，纵向
landscape 横向


CCT对前面三种进行了汉化, 分别是carticle, creport和cbook.
常用的选项有
10pt/11pt/12pt: 定义基准字号, 缺省10pt.
 twoside: 两面印刷格式, 因奇偶页装订位置不同而异, 缺省为单页.
  twocolumn: 双栏排版, 缺省为单栏.
  titlepage: 仅在article格式使用, 它是\maketile产生一个单独的文章题目页, 同时abstract也产生单独页
  leqno: 使公式标号出现在左边, 缺省在右
  fleqn: 公式左对齐, 缺省中间对齐
  thesis: 专用于毕业论文排版
  IEEE: 专向IEEE类杂志投稿的格式
  IFTHEN: 排版计算机程序

\columnsep 指定两栏间距
\columnseprule 两栏间竖线宽度，默认为0。
\mathindent 选择fleqn时 左边界的缩进量

以上参数修改用\setlength{\mathindent}{2.5cm}



# 

# 章节

\part,\chapter,\section,\subsection,\subsubsection,\paragraph,\subparagraph

`\命令[短标题]{标题} %用于显示在目录和页眉`
`\命令*{标题} %星号章节`

#### 层次

层次号：book中\part为-1（article中为0），\chapter为0，....
book类
\part，\chapter独立编号，只出现在奇数页，\part独占一页
\section，\subsection 关联编号
article类
\part，\section独立编号
\subsection，\subsubsection 关联编号
星号章节不参加自动编号
\part和\chapter标题占两行



#### 修改编号最深层次

\setcounter{secnumberdepth}{数}
secnumberdepth，book类-2～5，缺省为2，-2时取消编号
article类-1～5，缺省为3

#### 自动编号章节对应计数器

part，chapter，section，bsection,subsubsection,paragraph,subparagraph

#### 修改计数器值：

\setcounter{计数器名}{数}



# 版面

TeX中还经常会在\documentstyle和\begin{document}之间常用到很多修改版面尺寸的命令. 如未指明, 这些命令的格式都
是用\para_name=newvalue的格式.

 \texwidth, \texheight 主要正文body的宽度和高度, 不包括页眉页脚
 \oddsidemargin, \evensidemargin 奇数/偶数页, 纸张左边缘到页body左边缘的距离减去一英寸
 \topmargin 纸张上边缘到页眉或body(无页眉时)的距离减去一英寸
 \marginparwidth 页边注(marginnote)的宽度
 \marginparsep 正文边缘到页边注边缘的距离
 \headheight 页眉高度
 \headsep 页眉底部到页主体顶部的距离
 \footheight 页脚高度
 \footskip 页正文最后一行底到页脚底的距离
(建议, 总把\oddsizemargin（奇数页的左边界）\evensidemargin（偶数页的左边界）
\topmargin（从上页边到页眉的距离）设为0cm;
如果没用页眉, 将\headheight（页眉高度）,headsep（页眉基线到正文顶部的距离）设为0cm;
如果没用页脚, 将\footheight（已过时latex2e中已被去掉）,\footskip（正文底部到页脚底部的距离）设为0cm,
这样便于在输出时直接利用驱动程序的功能控制版心的位置.)

\columnsep 双栏article中, 左右栏间空白的距离
\columnseprule 双栏article中, 左右栏间分隔线的宽度, 缺省 为零, 即没有线
以下参数的修改可以在\begin{document}的前面和后面:
 \parskip 段落之间除了空出正常行距外额外空出的距离
 \parindent 段首空白的长度
 \footnotesep 两个注脚之间的距离
 \baselineskip 正文中前一行底和第二行底的距离, 会因字号的改变自动改变.另外, 定义行距还有一个特殊的参数, 那是\baselinestretch,它是用在\begin{document}前的全局变量, 修改格式如
\renewcommand\baselinestretch{倍数}    缺省时为1.0, 因此LaTeX中最小行距是\baselineskip乘上\baselinestretch得到的.

LaTeX的一个页面有页眉(head, 通常是杂志名, 卷号, 当前章节名等), 主体(body, 正文, 包括脚注及图表), 页脚(通常是
页码, 如果页码放在页眉处, 则页脚可能是空的). 我们用下面的
指令控制页版面:
 \pagestyle{参数}
参数可以是
  plain: 页码在页脚居中, 页眉空白, 为article, report的缺省
  empty: 页眉页脚都空白
  heading: 页脚为空, 页眉为正文的章节信息及页码
  myheadings: 自定义页眉, 内容由 \markboth{left_head}{right_head}   (双面twoside排版)或\markright{right_head}             (单面排版) \pagestyle是对全文有效的, 而如果要定义某页的页面格式,则可用\thispagestyle, 用法同上, 下一页自动恢复原设置.这里提到页码, 我们经常会修改页码的表现格式, 可能用阿拉伯数字或罗马数字等, 则修改\pagenumbering{参数}, 这里参
数可以是arabic(阿拉伯数字), roman(小写罗马数字: i, ii, iii,)Roman(大写罗马数字: I, II, III,), alph(小写英文: a, b, c,),
Alph(大写英文: A, B, C). 如果需要更改某页的页码, 则用修改计数器命令: \setcounter{page}{数字}, 这里page是页码计数器.

# 段落（分段、行距、水平间距、缩进命令）

强制分行：\\或\\*[和下行间距离]、\newline
建议分行：\linebreak[0-4，数越大建议力度越大]
\linebreak增加字间距，强制换行
\nolinebreak［n］建议不分行
\mbox｛内容｝内容保持在同一行

分段：\par，或两个回车
分页：自动分页
强制分页：\newpage
建议分页：\pagebreak［n］，\nopagebreak［n］

增加当前页高度有时可以避免难看的分页
\enlargethispage｛尺寸｝可增加的最大高度
\enlargethispage*｛尺寸｝指定增加高度

水平间距：
\quad 插入空白相当于当前字体大小
\qquad＝\quad×2
\ ，＝\quad×3/18
~=???好象比\ 小
\hspace{宽度大小}，\hspace*{宽度大小}
\hfill弹性长度：hspace{\hfill}插入空白，撑满整行
\hphantom{文本内容},占据文本内容的宽度
\vphantom[文本内容},\phantom{文本内容}

导引线：\dotfill，\hrulefill

垂直间距：
\vspace{高度}和\vspace*{高度}
\vfill：相当于\vspace{\fill}
\smallskip:-->\vspace{\smallskipamount}
\medskip:-->\vspace{\medskipamount}
\bigskip:-->\vspace{\bigskipamount}

段落首行缩进：
\setlength{\parindent}{2em},2个M
\setlength{\parindent}{0pt},首行不缩进
\CJKindent:两个汉字
\indent与\noindent
每节的第一段首行不会自动缩进
\hspane{\parindent}
在导言区加入：\usepackage{indentfirst}

段落间距：\lineskip+\parskip
可用\setlength修改以上值

行距：
\baselineskip：相邻两行基线间距离
\baselinestretch：伸展因子
修改改变行距：\renewcommand{\baselinestretch}[1.2]
放在\begin{document}之后，字体尺寸改变时才生效

# 标题

\title{标题可有\\换行}
\author{作者名可用and分开}
\date{日期可选，无命令自动当天日期，空白选项不显示}
\thanks{}可出现\maketitle以上任何位置，或几个\thanks
\maketitle
LaTex用特定字体、号居中输出

自定义标题环境
\begin{titlepage}
\end{titlepage}
生成标题独占一页，并重置页码计数器

#### 标题中文化

\renewcommand{\partname}{}
\renewcommand{\thepart}{第\，\Roman{part}}\,篇}

# 摘要

摘要环境
\begi{abstract}
...
\end{abstract}

book类没有摘要
摘要标题中文化
\renewcommand{abstractname}{摘\qquad 要}



# 数学环境

  |  本节内容: 三种数学环境, 数学环境中字体和字号, 数  |
  |  学公式中的空格, 上下标, 分式, \displaystyle, 大   |
  |  大小小的括号, 根式, 导数.                         

导言区加入数学公式宏包
\usepackage{latexsym}
\usepackage{bm}
\usepackage{amsmsth}
\usepackage{amssymb}

也可以并列
\usepackage{latexsym,bm,amsmsth,amssymb}

TeX提供三种有关数学公式的环境,：
第一种是"文中公式", 通过$或\(进入"数学环境", 通过$或\)来结束数学环境的; 
第二种是"独立公式", 用$$或\[进入"显示数学环境"(以后我们统称数学环境), 用$$或\]退出, 在正文, 它是独占一行的, 它排出的字体要稍微比文中公式要大些; 
第三种是带公式标号的数学公式: "方程",这个以后我们详细再讲. 数学环境是自动根据当前字号来调整公式中字的大小的.

数学环境中, 缺省字体是数学斜体(显示出来和意大利体一样),因此如果要用到正文, 需要改变字体或使用盒子, 如我们要输出"y=x, if x>0,"这一句, 其中的"y=0"和"x>0"应该是数学公式(虽然不进入数学环境也能输), 而"if"却属于正文内容, 因此不应该
用数学斜体显示, 而应该用"$y=x, {\rm if} x>0$"或用盒子:"$y=x, \mbox{if } x>0$", 但这里还要注意的是, 数学环境中忽
略一切空格(当然分隔命令的空格除外), 因此第一种输入可以发现,if和x>0之间没有我们想要的空格, 而第二种输入方式由于在\mbox{}中if后加了一个空格, 所以if和x>0有一个空格, 这正是我们想要的. 因此标准的输入方法一般用后者. 而且, 前者的方法对汉字就不适用, 因为汉字不能出现在数学环境中, 而用盒子框起来就没问题了. 这里再多说一句的是, 数学环境中不能使用字号命令,如果需要改变字号, 应该在数学环境之外改变, 而数学环境自动根据当前字号调整字的大小.

上面已经提到数学环境中忽略任何空白字符, 那么, 怎么在公式中输出空格呢? 当然我们可以用以前讲过的\quad或hskip来
空出横向空格等, 但是如果我们要输出诸如"fdx"(这里dx是微分),这样在f和dx中要有一个小空格, 用\quad显然太大了, hskip根本不知道该空出多大距离. 在公式中, 常用的几个调整距离的命令是"\,"(小距离), "\:"(中距离), "\;"(大距离), "!"(负距离),
象刚才说的例子, 我们一般就用$f\,dx$即可. 当然, 一般情况我们很少改变数学公式中的距离.

下面我们看看如何在数学公式中输入上下标, 在讲TeX保留字时大家就有印象了, 上下标分别用"^"和""来表示, 如$x_0^2$,
TeX中, 先输上标后输下标和先写下标再写上标是没有区别的, 它都会一样地自动调整字符大小和位置. 如果上下标的字符不止一个, 那就用"{}"括起来, 如$x^{1+y^{i+1}}$. 如果有人突然想在字符的左边输上下标呢? 简单的方法是在前面加一个空的{}, 如
${}{17}^{35}Cl$, 哦, 可能不是用的数学斜体, 那只好再用盒子了: ${}_{17}^{35}\mbox{Cl}$.

有时我们可能直接用1/2来表示分数就可以了, 但是如果分子分母我们想要排在分数线的上下, 那就要用"\frac{分子}{分母}"
来表示了, 如$$\frac{1}{x+1}$$. 但是大家如果再把这个例子用单$括起做文中公式, 或者$$y=\frac{y-\frac{1}{x+1}}{y+1}$$,
就会发现, 这个分式显示出来觉得比正常字号小, 要解决这个问题就要用\displaystyle的命令了. 你可以试试
$$y=\frac{y-\displaystyle\frac{1}{x+1}}{y+1}$$, 可以了吧.当然, 如果你在\documentstyle中使用了vatola选项(需要TeX系
统在指定目录有vatola.sty文件), 那么, 你可以直接用\dfrac来代替\frac来达到同样的效果, 而避免使用冗长的\displaystyle
的输入.(格式如\documentstyle[vatola]{article}; 而如果用\documentclass{article}, 则用\usepackage{vatola}); 或二
者均可以在第一句后面加上\input vatola.sty来包含这个包)有人可能又要问了, 如果我输出的分数, 分子还是有分子分母的分数, 分母也是一个不简单的分数, 那层层迭迭的分数线,不够美观, 我还是喜欢"分子/分母"的格式, 那怎么把这条斜分数
线画得长一些呢? 这里就要用到所谓的"定界符", 也就是成对出现的类似于括号的符号了, 如(), [], {}(用{和}输入), <>(用
\langle和\rangle输入), /, (用\backslash), |, ||(用|);以及另一些没法直接显示的符号, 大家自己用TeX产生出来看看:
$\lfloor, \rfloor; \lceil, \rceil; \uparrow; \Uparrow;\downarrow; \Downarrow; \updownarrow; \Updownarrow$. 这些
"括号"通常嵌套并和分数等数学公式一起使用, 如$$y=1+(\frac{(x+1)^2}{x^2})$$, 当然大家会看到这外层括号太
小, 不美观, 因此TeX提供了几个改变大小的命令, 从小到大依次是\big, \Big, \bigg, \Bigg, 如$$(, \big(, \Big(, \bigg(,
\Bigg($$, 其它定界符类似使用. 另外, TeX还提供了自动调整括
号大小的命令, 那就是在定界符前加\left和\right, 需要注意的是\left和\right一定要成对出现, 如果只用单个, 那么另一边就
要用"\left."或"\right."补上. 知道这些后, 我们就可以来输入长的"/"号了: $$\frac{1}{x+1} \left/ \frac{y+1}{x^2} \right.$$
或$$\left. \frac{1}{x+1} \right/ \frac{y+1}{x^2}$$, 这两个是不是比$$\frac{\displaystyle\frac{1}{x+1}}{\displaystyle
\frac{y+1}{x^2}}$$更令人满意啊?下面, 我们来讲讲根式的输入: "\sqrt[开方次数]{表达式}",

其中[开方次数]可选参数, 如果没有则是开平方, 如
$$\sqrt[3]{x+y}+\sqrt{2}$$.而导数, 也就是在字母右上方加一撇或两撇的输出, 我们常用

$$f^{\prime}$$和$$f^{\prime\prime}$$来表示, 或更简单地, 用
$$f'$$和$$f''$$来表示.
  +----------------------------------------------------+
  |  本节内容: 数学符号: 希腊字母, 二元运算符, 关系运  |
  |  算符, 箭头, 其它符号, 可用于一般环境的符号, 花体  |
  |  符号及函数名, 可变大小的符号, \limits和\nolimits, |
  |  省略号, 符号的上下堆积, 上下标的分行              |

#   控制符号

TeX提供了许多"控制符号"来得到诸如希腊字母, 关系运算符,箭头等无法用ASCII键盘直接输入的符号. 小写希腊字母, 如\alpha,\beta, \gamma, \pi; 大写希腊字母, 如\Gamma, \Pi, \Omega;二元运算符, 如\times(乘号), \div(除号), \pm(加减号), \circ(小圆圈), \cdot(点)等; 关系运算符, 如\leq(小于等于), \geq(大于等于), \subset(包含于), \supset(包含), \in(属于); 否
定关系运算符, 如\not=(不等于), \not<(不小于), \not\supset(不包含); 箭头, \leftarrow, \rightarrow, \longrightarrow,
\uparrow, \mapto等; 其它符号, \nabla(Nabla算子), \angle(角),\infty(无穷), \forall(任意), \exists(存在), \prime(导数的
撇). 这些符号比较多, 这里就不细细一一列出, 大家去找一本TeX书, 复印那两三页下来就可以了.

    本节讲的绝大多数符号都只能在数学环境中使用, 有几个符号
也可以使用在一般环境中, 那是\S(节号), \P(段落号), \dag(剑
号), \ddag(双剑号).

    有时数学公式中的函数名, 算子等要用特别的花体来排版,
TeX提供了\cal字体, 如"function $\cal F$". 而对于专有名词,
如一些函数名, 如sin x中的sin, 就要用罗马体, 而不是一般的
数学斜体排印, 我们可以用$${\rm sin}x$$, 也可以用TeX提供的
直接在函数名前加""的方法: $$\sin x$$, 一般的函数均有定义,
如\sin, \cos, \lim, \log等.

    数学环境中, 还有一类特殊的符号, 那就是可变大小符号, 如
求和号, 积分号, 它们会因为符号后面的内容的大小自动调整自己的大小: \sum, \prod, \coprod, \int, \oint, \bigcap, \bigcup,
\bigsqcup, \bigvee, \bigwedge, \bigodot, \bigotimes,\bigoplus, \biguplus. 需要注意的是, 有些可变符号的上下标位
置在文中公式和独立公式中是不一样的, 大家看个例子:$\sum{i=1}^n x_i=\int_0^\infty f(x)dx$和$$\sum{i=1}^n x_i=\int_0^\infty f(x)dx$$, 这里大家看到,\sum在文中公式中, 上下标是写在右上角和右下角的, 在独立公式
中, 是写在上面和下面的; 而\int在二者中都写在右上角和右下角的. 我们可以强制用\limits和\nolimits来控制上下标的出现位置:
使用方法如$\sum\limits_{i=1}^b x_i$就强制将上下标写在上边和下边, 而\nolimits使其出现在右边角上. 这里多说一句, 如果
你想把一般的操作符也想用\limits或\nolimits用, 只须把你的操作符用\mathop{}括起来即可.

    大家如果编排矩阵或行列式, 就会遇到特别的省略号, 大家试
试\cdots, \vdots, \ddots就是三个方向的省略号. 而\ldots是比
\cdots低一点的省略号, 它和其它三个不同的是也可以用在正文环
境中. \ldots一般用于$x_1, x_2, \ldots, x_n$这样的时候.

    排版数学公式可能还会遇到需要把两个符号上下组合在一起,
最常见的就是上划线和下划线, 大家试试$$\overline{a+b+c+d}$$
和$$\underline{a+b+c+d}$$, 这里需要说明的是, \overline只能
用于数学环境, 而\underline也可以用在正文中. 类似地还有用花
括号括在式子上下的: $$\overbrace{a+\underbrace{b+c}+d}$$,
而如果上下括号上面或下面还有符号, 可以用上下标来表示, 如:
$$\overbrace{a+\underbrace{b+c}_{1.0}+d}^{2.0}$$. LaTeX还
可以将任意两个符号重叠在一起: \stackrel{上层符号}{下层符号},
如$$\vec{x} \stackrel{\rm def}{=}(x_1, x_2, \ldots, x_n)$$,
这里需要说明的是\stackrel中第一个参数的符号以较小字号输出的.
而$${上面 \atop 下面}$$可以把两行内容按相同字号排出, 类似
地就出现了$${n \choose m}$$则是带括号的n个取m个的写法.

    符号可以上下堆积, 可是我们如果要在\sum的下面写诸如i<9
和j<9这两行下标, 用$$\sum{i<9 \ j<9} i/j$$是不行的. 我们
怎么实现这样的分行呢? 我们可以用\atop来堆积, 如
$$\sum{\scriptstyle i<3 \atop \scriptstyle j<3} i/j$$
这里之所以加了\scriptstyle是因为仅用\atop命令会把上下的字
体再缩小一号. 另外, 我们也可以用另外的方法: 前面我们在讲
\frac时提到\dfrac这个符号需要使用包vatola.sty, 这里, 如果
使用了vatola.sty这个包, 我们可以在下标中用{\Sb 第一行 \
第二行 \endSb}, 在上标中用{\Sp 第一行 \ 第二行 \endSp}来
表示多行下标或上标.


  |  本节内容: 数组array, 方程(标号)equation, 多行方程 |
  |  eqnarray, \aligned(vatola.sty), 标号的交叉引用    |
  |  参考文献的使用(more)                              |
  +----------------------------------------------------+

# 数组环境

数组环境通常用来编排矩阵, 行列式等对齐的数学公式的.

它的格式是:
\begin{array}{列对齐}
第一行 \
第二行 \
...
最后一行
\end{array}
这里, 列对齐的格式是{c1c2c3...cn}, 每个ci为一个字母, 说明第i列的对齐方式, 可以是c(居中), l(左对齐), r(右对齐). 而
每一行的各列用&符号隔开, 行末是\. 因此n列的数组, {列对齐}应该有n项, 每行应该有n-1个&, 一个\(最后行通常不用\). 数
组中某一列可以不存在, 但是&号不能少. 数组外常常使用可变大小的定界符\left和\right, 大家看个例子:

```tex
$$\left(
\begin{array}{clr}
a+b+c & a+b+c & a+b+c \
a+b & a+b & a+b \
a & a & a
\end{array}
\right) $$
```



这里要作些说明, 数组中某两行的距离可以用"\\[距离]"来改变, 也可以用"\renewcommand\arraystretch{实数}"来整体修
改数组的垂直距离(缺省为1.0), 而参数\arraycolsep=...是修改其列间距. 使用数组时, 经常容易出错的是: array必须出现在数
学环境中, &的个数和\的个数一定要正确, 如果使用可变大小的括号, 一定要注意\left和\right必须成对出现, 即使只排印半对
括号.

一般的$和$$环境, 不能给公式或方程编号, 因此, 就用到了方程环境. 格式是:
\begin{equation}
方程
\end{equation}
这其中的方程, 和$$情况没有两样, 只是在公式右边自动加上了方程编号(如果\documentstyle用了\leqno选项, 则公式标号在左边). 多行的方程可以把array使用在equation中来实现, 但是标号只出现一个, 出现在多行的中间. 如果多行要分别标号, 或者
不想用麻烦的$$嵌套array, 那就要用到多行方程环境:
\begin{eqnarray}
......
\end{eqnarray}
和
\begin{eqnarray}
...
\end{eqnarray}
二者的区别是, 带号的不将公式标号排出来, 而不带的自动给每行式子编排标号. 在\begin{eqnarray}和\end{eqnarray}中的
部分是一个三列的array环境, 因此有两个&和一个\, 如:
\begin{eqnarray}
y&=&1+2+3+4+5+6+7+8+9+10 \
&=&55
\end{eqnarray}
而如果把方程某行的\前加上"\nonumber", 则TeX不给该行方程
编排标号, 如"y&=&1+2+3+4+5+6+7+8+9+10 \nonumber \", 则该
行不出现标号. 这里还要注意的是equation和eqnarray都是直接
进入$$的显示数学环境, 因此不能在前面和后面加上$或$$了.

    大家可能会注意到, 不论是array还是eqnarray, 每个&符号
都会在公式中产生列的小空隙, 同样也在vatola宏库中, 定义了
一个aligned对齐环境, 它使得编排多行公式在对齐的同时不会出
现$符号位置的列空隙. 它可以出现在$$环境中, 那公式不标号;
或出现在equation中, 它对一个多行公式只标一个标号, 类似于
array. 它相当于一个两列的array, 因此每行仅有一个&.
\begin{equation}
\aligned
y&=1+2+3+4+5+6+7+8+9+10 \
&=55
\endaligned
\end{equation}
这里需要注意的是, \begin{array} \end{array}和\begin{tabular}
(制表)\end{tabular}不能出现在\aligned与\endaligned中, 如须
使用, 要用\vbox{}或\hbox{}等把array或tabular环境括起来.

    在讲第一个完整的TeX文档例子时, 大家一定注意到参考文献
标号的交叉引用, 而方程也有标号, 也可以交叉引用. 为什么我
们选择交叉引用而不是直接在文中写"公式(1)中..."的原因很简
单, 交叉引用可以实时地调整标号, 插入或删去一个公式带来整
体标号的改变, 无需改变引用标号的地方; 而且, 可以在不修改
正文的情况下灵活地调整标号的风格.

    TeX使用\lable{标号}来定义标号, 这里的标号可以是字母,
数字, 标点等组成的字符串. 需要引用, 则使用\ref{标号}, 这
里的"标号"应该是有\lable定义过的, 定义和引用的先后无关.
例如, 我们有
\subsection{Early Results}
\label{sec-early}                       %这里定义子节标号
Euler's equation
\begin{equation}
e^{i\pi}+1=0 \label{eq:euler}           %这里定义方程标号
\end{equation}
\combines the five most important numbers in mathematics
in a single euqtion.
然后我们就可以如下地引用
Equation~\ref{eq:euler} in Section~\ref{sec-early} ...
不管这里方程或子节的标号是多少, 引用时都能准确地指出. 这
就是我们要使用自动交叉引用的原因. 这里, \label会自动根据
自己的位置, 得出标号, 如出现在equation, eqnarray, enumerate
(项目), figure(图), table(表)环境中, 被引用的是公式号, 项
目编号或图表号; 而出现在其它位置则是章节号.

    引用时除了\ref外还有一个\pageref{标号}, 它显示的是
\label{标号}出现的页面位置.

    \cite和\bibitem我们在一开始的例子中就看到了, 我们这里
更详细地说说这两条命令的完整格式:
\cite[附加信息]{标号1, 标号2, ..., 标号n}
\bibitem[名称]{标号}
先看一个\cite加附加信息的例子(这个例子是在第5节例子的参考
文献的基础上的):
See \cite{texbook, companion} or \cite[page 20-22]{lamport} ..
再看\bibitem的名称可选项:
See \cite{kn:texbook} for more details.
...
\begin{thebibliography}[lamport 86]     %[]中是最长文献编号
\bibitem[Knuth 84]{kn:texbook} D. E. Knuth. {\sl The \TeX{}book}.
Addison-Wesley, Reading.
\end{thebibliography}

    这里再多说一句的是: 所有涉及交叉引用的文件, 在修改过与
交叉引用有关的内容之后, 都需要对源文件进行两次编译才能得到
正确的结果.

# 环境

  本节内容: 居中, 左对齐, 右对齐环境; 小页环境; 抄录环境; 列表环境; 制表环境.这里要介绍的是几个TeX中常用的环境, 它的一般格式是:

\begin{环境名}
...
\end{环境名}

首先是居中, 左对齐, 右对齐环境, 这三者的环境名分别是center, flushleft和flushright, 在环境中的正文以\断行. 这
三个环境比较简单, 就不举例子了. 需要注意的是, 紧接这环境后的正文和环境如果没有空行隔开, 那么系统认为是一个段落,
就是说环境后的正文行首没有\parindent的缩进.

 abstract就是小页. 小页环境的格式是:
\begin{minipage}[位置]{宽度}
...
\end{minipage}
{宽度}可以用TeX的任何合法距离; [位置]是可选项, 可以选择t
或b来表示小页是和正文是"顶部对齐"还是"底部对齐", 请看例子:
```tex
NORMAL TEXT
\begin{minipage}[b]{1 in}
This is a minipage aligned on its bottom line.
\end{minipage}
AND
\begin{minipage}[t]{1 in}
This is a minipage aligned on its top line.
\end{minipage}
END
```

注意的是, 小页的footnote(脚注)是紧跟在小页后面, 而不是在
整个页面的下面, 所以在minipage嵌套时, 可能系统会放错脚注
的位置.

抄录环境(verbatim)在\begin{verbatim}和\end{verbatim}

的任何字符都将原样输出, 包括\等TeX保留字. 而"verbatim"与
verbatim的区别是, 它将把空格用|_|表示出来. verbatim有一个
简写形式, "\verb标识符 字符串 标识符", 其中标识符可以是空
格以外任何字符, 它与\verb之间没有空格. 如:
\verb+
This is !@#$%%^&&*({ All you want to type.
+
当然, 字符串里就不能出现你作为标识符的符号了.

列表环境itemize, enumerate, description.

\begin{itemize}
\item 列表项1
\item 列表项2
...
\item 列表项n
\end{itemize}
自动编号; 如果超过一行, 自动缩进以突出编号. 而enumerate与
itemize的区别是, 它不出现数字编号, 而是以小黑圆点来标识.
description一般用于类似于名词解释的情形:
\begin{description}
\item[名词] 解释
\item[名词] 解释
...
\end{description}
一般, 还在[名词]中加上\bf或\heiti以突出名词.
列表环境还可以嵌套使用, 具体就不细述了.

# 表    格

表格环境tabular

\begin{tabular}[竖向位置]{列格式}
....
\end{tabular}
竖向位置：t、b 缺省居中
列与列间用&分隔，每行\[长度：改变行间间隔]结束
列格式：l左对齐，c居中，r右对齐
边界线：｜，｜｜

横线：
\hline
\cline{m--n} m--n列水平线
\nline与行等高竖线

\multicolumn{列数}{列格式}{文本内容}
列数＝1时，改变当前列对齐方式

TeX专门提供了一个制表环境, 用来排印有线或无线的表格.

\begin{tabular}[位置]{列定义}
...
\end{tabular}
这里[位置]和minipage一样, 可选t或b, 但我们通常用的表格都是独立表格, 所以通常不定义位置, 而直接独立一段. {列定义}
类似于array的列对齐, 可以用c,l和r来表示对齐方式, 这里的列定义还可以在列对齐字母间用"|"以画出表格中列的竖线. 表格内
容如array一样, 用&隔开, \换行, 同样要注意&的个数. 表格的横线可以用\hline来表示, 如:
\begin{tabular}{|c|c|c}
\hline
1 & 2 & 3 \
\hline
4 &   & 6 \  %这里要注意, 若最后行要画横线, 则此处要有\
\hline
\end{tabular}
而"\cline{列号1-列号2}"则是表示从列号1到列号2的一条横线.而如果要在表格元素中画竖线, 则可以用"\vline". 有时我们还会遇到需要把某行表格的几列合并起来, 这就要使用
\multicolumn{栏数}{栏定义}{内容}
{栏数}是要合并的栏的数目, {栏定义}类似于表格的{列定义}, 如:
\begin{tabular}{|c|c|c|}
\hline
\multicolumn{2}{|c|}{1} & 2 \
\hline
3 & 4 & 5 \
\hline
\end{tabular}
而
\begin{tabular}{宽度}[位置]{列定义}
...
····\end{tabular}可以自己定义表格的总宽度, 如\textwidth等TeX的合法距离.

最后, 我们讲讲制表环境的四个参数, 这四个参数都是局部参数, 也就是说只要用   分组限定命令的作用范围, 就可以调整某
个表格的参数而不影响其它表格. \tabcolsep是两列间水平距离的一半, 缺省为6pt; \arrayrulewidth为定义\hline, \vline,
\cline及列定义的分隔线|的线宽, 缺省为0.4pt; \doublerulesep为连续两个\hline或列定义中连续两个|所画的线段之间的间隔,
缺省为2pt, 如果设为0pt, 则可以用连续的\hline或|来加粗表格的某些线框; \arraystretch是一个实数, 缺省为1.0, 定义行距
的一个因子, 用\renewcommand来改变.