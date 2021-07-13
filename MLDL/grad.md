None
None
http://www.itboth.com/d/e2mYJn

https://www.cnblogs.com/xiaojianliu/articles/9649037.html

深度学习的优化算法，说白了就是梯度下降。每次的参数更新有两种方式。

第一种，遍历全部数据集算一次损失函数，然后算函数对各个参数的梯度，更新梯度。这种方法每更新一次参数都要把数据集里的所有样本都看一遍，计算量开销大，计算速度慢，不支持在线学习，这称为Batch gradient descent，**批梯度下降**。

另一种，每看一个数据就算一下损失函数，然后求梯度更新参数，这个称为**随机梯度下降**，stochastic gradient descent。这个方法速度比较快，但是收敛性能不太好，可能在最优点附近晃来晃去，hit不到最优点。两次参数的更新也有可能互相抵消掉，造成目标函数震荡的比较剧烈。

为了克服两种方法的缺点，现在一般采用的是一种折中手段，**mini-batch gradient decent**，小批的梯度下降，这种方法把数据分为若干个批，按批来更新参数，这样，一个批中的一组数据共同决定了本次梯度的方向，下降起来就不容易跑偏，减少了随机性。另一方面因为批的样本数与整个数据集相比小了很多，计算量也不是很大。



# 最速梯度下降法BSD
又称批量梯度下降法 Batch Gradient Descent
${ \partial J( \theta ) \over \partial \theta_j }=-{1 \over m} \sum \limits _{i=1}^m (y_i - h_\theta(x_i))x_j^i$

沿导数相反的方向移动theta


# 随机梯度下降SGD




# Mini-batch Gradient Descent

# 带Mini-batch的SGD

（1）选择n个训练样本（n<m，m为总训练集样本数）

（2）在这n个样本中进行n次迭代，每次使用1个样本

（3）对n次迭代得出的n个gradient进行加权平均再并求和，作为这一次mini-batch下降梯度

（4）不断在训练集中重复以上步骤，直到收敛。
