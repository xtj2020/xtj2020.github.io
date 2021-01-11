<script src="ut.js" type="text/javascript"></script>

# 文献阅读

## 阅读RIADD有关文献

###  代码查询

- <https://www.semanticscholar.org/>这个网站可以提供的信息包含但不受限于论文公开的Github上的代码实现，包括其他人的复现论文被接受的Conference /Journal 和时间论文的引用情况，高引用情况，近几年引用的情况被Media Mentions(推特，博客之类的)Similar papers（这个特别特别棒！）尤其是在想深入了解该领域的前沿工作的时候
- <https://paperswithcode.com/>集合了arXiv上最新的机器学习研究论文，而且关联了这些论文在GitHub上的代码。
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

------

文件名：1803.04337v3.pdf \
标题：Replication study: Development and validation of a deep
learning algorithm for detection of diabetic retinopathy in
retinal fundus photographs \
主要工作：试图在JAMA 2016发表的视网膜眼底照片中复制和开发用于检测糖尿病性视网膜病的深度学习算法的主要方法

源代码：<https://github.com/mikevoets/jama16-retina-replication>tensorflow

------

文件名：Reproduction study using public data of:
Development and validation of a deep
learning algorithm for detection of diabetic
retinopathy in retinal fundus photographs.pdf \
标题：Reproduction study using public data of:
Development and validation of a deep
learning algorithm for detection of diabetic
retinopathy in retinal fundus photographs \

主要工作：开发和验证用于检测眼底照片中的糖尿病性视网膜病变的深度学习算法PLOS ONE 2019•Mike Voets•KajsaMøllersen•Lars Ailo Bongo我们试图将其的结果复制和验证
《深度学习算法》，用于检测视网膜眼底照片中的糖尿病性视网膜病变，发表于JAMA 2016; 

源代码：<https://github.com/mikevoets/jama16-retina-replication> tensorflow

------

文件名：1706.03008v2.pdf \
标题：An Ensemble Deep Learning Based Approach for Red Lesion Detection in
Fundus Images \
主要工作：处理红色病变，在本文中，我们提出了一种结合深度学习和领域知识的红色病变检测的新方法。 
CNN学习的功能通过合并手工制作的功能得到增强。
随后使用描述符的这种集成向量，使用随机森林分类器来识别真正的病变候选者。
我们从经验上观察到，结合两种信息来源，相对于分别使用每种方法，可以显着改善结果。
此外，与第二位人类专家相比，我们的方法在DIARETDB1和e-ophtha上报告了基于病灶的最高性能，并且筛选和需要在MESSIDOR上转诊。

源代码：<https://github.com/ignaciorlando/red-lesion-detection>


------
文件名：2007.14456v1.pdf

标题：Enhancement of Retinal Fundus Images via Pixel Color Amplification

主要工作：通过像素颜色放大增强视网膜眼底图像2020年7月28日•Alex Gaudio•Asim Smailagic•AurélioCampilho我们提出了像素颜色放大理论和一系列增强方法，以促进视网膜图像的分割任务。
我们对除雾理论基础的图像失真模型的新颖重新解释显示了除雾社区常用的三个现有先验与新颖的第四先验之间的关系。
我们利用该理论为视网膜图像开发了一系列增强方法，包括使整个图像变亮和变暗的新颖方法。
我们展示了Unsharp Masking算法的新颖派生。
我们评估了增强方法，将其作为具有挑战性的多任务分割问题的预处理步骤，并显示出所有任务的性能大幅提高，Dice分数在无增强基线的基础上增加了0.491。
我们提供的证据表明，我们的增强预处理对于不平衡和困难的数据很有用。
我们展示了这些增强功能可以通过将它们组合在一起来执行类平衡。

<https://github.com/adgaudio/ietk-ret>

-----
文件名：2001.01815v1.pdf \

标题：Regression and Learning with Pixel-wise Attention for Retinal Fundus Glaucoma Segmentation and Detection \
主要工作：眼科医生观察视网膜眼底图像是青光眼的主要诊断方法。
然而，仅通过手动观察仍难以区分病变特征，尤其是在青光眼早期。
在本文中，我们提出了两种基于深度学习的自动算法，用于青光眼的检测以及视盘和杯的分割。
我们利用注意力机制来学习像素级特征以进行准确的预测。
特别是，我们提出了两个卷积神经网络，它们可以专注于学习各种像素级特征。
此外，我们制定了几种注意力策略来指导网络学习对预测准确性有重大影响的重要特征。
我们在验证数据集上评估我们的方法，提出的两个任务的解决方案都可以取得令人印象深刻的结果，并且胜过当前的最新方法。

源代码：
- <https://github.com/cswin/RLPA>
- <https://github.com/archit31uniyal/DC-Gnet>



----

文件名：1809.05216v1.pdf
标题：Enhanced Optic Disk and Cup Segmentation
with Glaucoma Screening from Fundus Images
using Position encoded CNNs


主要工作：使用位置编码的CNN从眼底图像中筛选青光眼的增强型视盘和杯状分割14 Sep 2018•Vismay Agrawal•Avinash Kori•Varghese Alex•Ganapathy Krishnamurthi在本手稿中，我们提出了一种可靠的方法，用于从眼底图像中选择青光眼
卷积神经网络（CNN）。
该管道包括首先从眼底图像中分割视盘和视杯，然后提取以视盘为中心的斑块，然后将其馈送到分类网络以区分图像为患病图像还是健康图像。
在分割网络中，除了图像之外，我们还利用空间坐标（X \＆Y）空间来更好地学习感兴趣的结构。
分类网络由DenseNet201和ResNet18组成，它们在大量自然图像上进行了预训练。
在REFUGE验证数据（n = 400）上，分割网络的视盘和视杯的骰子得分分别为0.88和0.64。
对于区分受青光眼影响的图像和健康图像的任务，ROC曲线下的面积为0.85。 

源代码:<https://github.com/koriavinash1/Optic-Disk-Cup-Segmentation> pytorch

## 无源代码论文
-----

文件名:du2020  \
标题：Computer Methods and Programs in Biomedicine \
主要工作：自动检测眼底图像中的视网膜微动脉瘤（MA）


------

文件名：Automatic Detection of Hard Exudates in Retinal Fundus Images.pdf \
标题：Automatic Detection of Hard Exudates in Retinal Fundus Images
主要工作：检测眼底中的渗出液

文件名：1808.03656.pdf \
标题：Detection of Hard Exudates in Retinal Fundus \
作者：Avula Benzamin, Chandan Chakraborty \
Images Using Deep Learning
主要工作：检测硬质渗透液来判断是否有DR


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


参考意义：
- 可以用传统方法实现血管、视盘的移除并分割出硬性渗出液

-----
文件名：10.1016@B978-0-12-817440-1.00002-4.pdf \
标题：Deep learning approach for
classification of eye diseases
based on color fundus images \
作者：Bambang Krismono Triwijoyoa,b, Boy Subirosa Sabargunaa,
Widodo Budihartoa, Edi Abdurachmana 

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

------
文件名：F9905038620.pdf \
标题：Identification of Diabetic Retinopathy from Color Fundus Images using Deep Convolutional Neural Network \
作者：Bansode Balhim Narhari, Bakwad K.M., Ajij Dildar Sayyad \
主要工作：
- 提供了一种基于预先检查的完全卷积神经网络（CNN）并通过转移学习完成的创新技术。
最后，利用支持向量机分类器，从最近的深度CNN模型中有效学习。
同时，额外的视网膜图像预处理技术被应用以获得更好的分类结果。
改进的结果为视网膜筛查系统的计算机辅助诊断领域做出了贡献


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
