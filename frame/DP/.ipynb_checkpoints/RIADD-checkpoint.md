<script src="ut.js" type="text/javascript"></script>

# 文献阅读

## 阅读RIADD有关文献

###  代码查询

- <https://www.semanticscholar.org/>这个网站可以提供的信息包含但不受限于论文公开的Github上的代码实现，包括其他人的复现论文被接受的Conference /Journal 和时间论文的引用情况，高引用情况，近几年引用的情况被Media Mentions(推特，博客之类的)Similar papers（这个特别特别棒！）尤其是在想深入了解该领域的前沿工作的时候
- <https://paperswithcode.com/>paperswithcode集合了arXiv上最新的机器学习研究论文，而且关联了这些论文在GitHub上的代码。

- <https://researchcode.com/>一个很好用的查找论文代码的网站，当您在arxiv.或Google Scholar中搜索浏览论文时，还可以用chrome扩展程序”ResearchCode code finder“查找代码。 


1.寻找论文作者的个人主页在google搜索该论文的名称加上论文作者的姓名，找到目标作者的个人主页。一般在他们的个人主页上都有可能看到论文的链接和代码。我在寻找论文和代码的过程中，发现作者的主页上会有在其他网站暂时还找不到的论文和该论文的源码。


2.改变关键字 开发语言+论文的关键字牛人一般都会想办法证明下自己有多牛，也会自己动手去尝试实现别人论文的代码，所以换关键字后也有可能找到正好是你需要的code，不过是其他牛人的杰作。

3.直接联系本人
<https://academia.stackexchange.com/questions/26159/can-i-request-the-code-behind-a-research-paper-from-the-author>





### 博客

进行小目标检测文献综述<https://zhuanlan.zhihu.com/p/138108192>

把深度学习网络作为特征提取器（Feature Extractor）来使用，将提取出的深度学习特征，输入传统的经典分类器，进行分类。



眼底血管形态学阈值分割（有代码，cv2传统方式）<https://blog.csdn.net/virus1175/article/details/107126348>


## 有源代码论文
-----

文件名：1906.11143v2.pdf \
标题：Boundary and Entropy-driven Adversarial
Learning for Fundus Image Segmentation \
主要工作：
- 来自不同数据集的眼底图像中的视盘（OD）和杯（OC）的正确分割对于青光眼疾病筛查至关重要。在这项工作中，我们提出了一种无监督的领域自适应框架，称为边界和熵驱动的对抗学习（BEAL），以改善OD和OC的分割性能，尤其是在模糊边界区域上。

源代码：<https://github.com/EmmaW8/BEAL> pytorch版

-----

文件名：1805.07549v1.pdf \
标题：Disc-aware Ensemble Network for Glaucoma 
Screening from Fundus Image \
主要工作：
- 还是利用杯盘比
- 本文中，我们介绍了一种深度学习技术来获取其他图像相关信息，并直接从眼底图像中筛选青光眼。
具体而言，提出了一种新颖的用于自动青光眼筛查的碟片感知集合网络（DENet），该网络将全球眼底图像和局部视盘区域的深层次背景进行了整合。
在不同级别和模块上的四个深层流分别被认为是全局图像流，分段引导网络，本地磁盘区域流和磁盘极性转换流。
最后，将不同流的输出概率融合为最终筛选结果。

源代码：
- <https://github.com/HzFu/MNet_DeepCDR> tensorflow
- <https://github.com/HzFu/DENet_GlaucomaScreen> tensorflow
- <https://github.com/Aniladepu007/Joint-Optic-Disc-and-Cup-Segmentation-Based-on-Multi-Label-Deep-Network-and-Polar-Transformation> keras



### 无源代码论文
-----

文件名:du2020  \
标题：Computer Methods and Programs in Biomedicine \
主要工作：自动检测眼底图像中的视网膜微动脉瘤（MA）


源代码：无

------

文件名：Automatic Detection of Hard Exudates in Retinal Fundus Images.pdf \
标题：Automatic Detection of Hard Exudates in Retinal Fundus Images
主要工作：检测眼底中的渗出液

文件名：1808.03656.pdf \
标题：Detection of Hard Exudates in Retinal Fundus \
作者：Avula Benzamin, Chandan Chakraborty \
Images Using Deep Learning
主要工作：检测硬质渗透液来判断是否有DR

源代码：无

-----

文件名：eadgahi2012.pdf \
标题：Localization of Hard Exudates in Retinal Fundus Image by \
Mathematical Morphology Operations 
作者：Mehdi ghafourian fakhar eadgahi，Hamidreza pourreza \
主要工作：
- 本文提出了一种基于形态学的视网膜彩色图像中硬质渗出物的分割方法。在所提出的方法中，对视网膜图像进行预处理，并首先识别视盘和血管，然后从图像中消除它们。 

工作基础：
- 使用形态学上的闭合算子来移除血管。
然后使用熵特征来查找和删除视盘区域。
最后，他们通过扩张操作使用形态重建来分割硬性渗出液。

源代码：无

参考意义：
- 可以用传统方法实现血管、视盘的移除并分割出硬性渗出液

-----
文件名：10.1016@B978-0-12-817440-1.00002-4.pdf \
标题：Deep learning approach for
classification of eye diseases
based on color fundus images \
作者：Bambang Krismono Triwijoyoa,b, Boy Subirosa Sabargunaa,
Widodo Budihartoa, Edi Abdurachmana \

主要工作：看看工作基础内的文章

工作基础：
- Palomera-P erez等人的研究[16]提出了视网膜血管的自动分割。 
- Sivakumar提出了使用视觉神经-视觉中性光谱成分对糖尿病性视网膜病变进行分类的方法[17]。 
- Marı´n等人的进一步研究。 
[13]还提出了人工神经网络来检测糖尿病性视网膜病变。 
- Ricci和Perfetti [18]提出了使用SVM来检测作为糖尿病性视网膜病症状的视网膜眼出血的方法。 
- Usher等人提出了数字化视网膜图像中糖尿病视网膜病变自动检测系统的开发及其在糖尿病视网膜病变筛查中的潜在价值。 
[19]。 
- Mohamed [20]使用先进的饲料神经网络进行了用于诊断的糖尿病性视网膜病变智能自动检测系统。

源代码：无

------
文件名：F9905038620.pdf \
标题：Identification of Diabetic Retinopathy from Color Fundus Images using Deep Convolutional Neural Network \
作者：Bansode Balhim Narhari, Bakwad K.M., Ajij Dildar Sayyad \
主要工作：
- 提供了一种基于预先检查的完全卷积神经网络（CNN）并通过转移学习完成的创新技术。
最后，利用支持向量机分类器，从最近的深度CNN模型中有效学习。
同时，额外的视网膜图像预处理技术被应用以获得更好的分类结果。
改进的结果为视网膜筛查系统的计算机辅助诊断领域做出了贡献

源代码：无

-------




## 图像的预处理方法



## 数据集的描述


## 小目标处理（比较小的目标）

- 利用滑窗


## 比较明显的目标（用神经网络直接分类）

## 特征提取+分类

### 用影像组学的方法提取特征

### 用传统数学方法提取特征

### 用机器学习方法提取特征


## 特征融合


## 特征分类


# 训练角度


##  对数据的分析



##  对某个网络的熟悉


## 文档的编撰能力
