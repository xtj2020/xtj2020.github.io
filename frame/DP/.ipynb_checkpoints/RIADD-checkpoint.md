# 文献阅读

## 阅读RIADD有关文献

### 博客

进行小目标检测文献综述<https://zhuanlan.zhihu.com/p/138108192>

把深度学习网络作为特征提取器（Feature Extractor）来使用，将提取出的深度学习特征，输入传统的经典分类器，进行分类。



眼底血管形态学阈值分割（有代码）<https://blog.csdn.net/virus1175/article/details/107126348>



### 论文

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
然后使用熵特征来查找和删除光盘区域。
最后，他们通过扩张操作使用形态重建来分割硬性渗出液。
- 无源代码

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
------
文件名：F9905038620.pdf
标题：Identification of Diabetic Retinopathy from Color Fundus Images using Deep Convolutional Neural Network
作者：Bansode Balhim Narhari, Bakwad K.M., Ajij Dildar Sayyad

-----

文件名：quellec2020.pdf
标题：Automatic detection of rare pathologies in fundus photographs using few-shot learning
作者：GwenoléQuellec a , Mathieu Lamard b , a , Pierre-Henri Conze c , a , Pascale Massin d , Béatrice Cochener

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
