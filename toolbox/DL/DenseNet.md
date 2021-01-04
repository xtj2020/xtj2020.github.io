设计理念：create short paths from early layers to later layers

一般的卷积网络连接为n连接，而DenseNet为n*(n+1)/2个连接

为什么参数会减少？

与ResNet的区别？

基本的结构是怎么样的？


highway网络

higway灵感来自于LSTM门机制，允许信息高速无障碍地通过深度神经网络各层。应用在词情感分析上。
内在逻辑公式：
$ H(x,W_H)T(x,W_T)+xC(x,W_C)$

https://zhuanlan.zhihu.com/p/38130339

https://zhuanlan.zhihu.com/p/35019701

https://blog.csdn.net/l494926429/article/details/51737883

ResNet网络

越深的网络效果越好，但是到达某一种程度后效果不降反升，这种被称为“退化”。处理方法有：“快捷连接”、降采样处理。

神经网络维度更深的化能够将特征映射到更高的维度上，但是维度变深了，其恒等变换受到影响了。

https://zhuanlan.zhihu.com/p/101332297

https://www.cnblogs.com/shine-lee/p/12363488.html

# 参考文献
https://blog.csdn.net/u014380165/article/details/75142664
