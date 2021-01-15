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
