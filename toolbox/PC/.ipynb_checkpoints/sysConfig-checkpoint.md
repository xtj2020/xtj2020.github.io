# 系统配置(system)

## jpyter系统配置

```python
#设置密码与指定端口
c.NotebookApp.password=u'sha1:6c9e6e11ed'
c.NotebookApp.port = 9999
#使得所有机器都能连接
c.NotebookApp.allow_remote_access = True
c.NotebookApp.ip='*'
#默认不打开浏览器
c.NotebookApp.open_browser = False
#使用指定文件配置jupytermotebook
jupyter notebook --config jupyter_notebook_config_2.py
#即使断开连接也能够继续运行
nohup jupyter notebook &
```


## 使用kaggle下载

```
pip install kaggle
在我的账号里找到kaggle.json文件，放入～.kaggle目录下
然后同意数据集协议，复制下载命令，对数据集进行下载
```


## pytorch的配置

查询N卡的算力，匹配对应的显卡驱动
https://developer.nvidia.com/cuda-gpus#compute
显卡驱动对应的CUDA
https://developer.nvidia.com/cuda-toolkit-archive
CUDA对应的cuCUDA
https://developer.nvidia.com/rdp/cudnn-archive

# github与解析网页

在阿里云万网上购买一个域名
对域名进行解析，第一个解析对应github.io，第二个解析对应具体ip值，ip值可以通过网站查询得到
在github上建立一个CNAME的文件，写入域名，不带http://,并上传至文件夹。

# gpustat动态监控gpu
pip install gpustat \
watch --color -n1 gpustat -cpu 

# GPU知识
<https://blog.csdn.net/TTdreamloong/article/details/84886621>
<https://zhuanlan.zhihu.com/p/31558973>

计算单位flop：浮点数先乘后加算一个flop

1Byte = 8 bit
1Word = 2 Byte
1K = 1024 Byte
1M = 1024 K
1G = 1024 M
1T = 1024 G

10 K = 10*1024 Byte

# wget

<https://blog.csdn.net/tylai520/article/details/17168673>

wget -r -p -np -k -P ~/tmp/ http://java-er.com

```python
解释一下参数

-P 表示下载到哪个目录
-r 表示递归下载
-np 表示不下载旁站连接.
-k 表示将下载的网页里的链接修改为本地链接.
-p 获得所有显示网页所需的元素

额外的
-c 断点续传
-nd 递归下载时不创建一层一层的目录，把所有的文件下载到当前目录
-L 递归时不进入其它主机，如wget -c -r www.xxx.org/
-A 指定要下载的文件样式列表，多个样式用逗号分隔
-i 后面跟一个文件，文件内指明要下载的URL

```
