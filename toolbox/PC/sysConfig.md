# 系统配置(system)

## jpyter系统配置

### 修改配置文件

```python
jupyter notebook --generate-config
vi ~/.jupyter/jupyter_notebook_config.py

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
# 更改默认目录
c.NotebookApp.notebook_dir = u'需要默认的路径' 
```


### 创建密码
jupyter notebook password

/home/xtj/.jupyter/jupyter_notebook_config.json

from notebook.auth import passwd

passwd()

'argon2:$argon2id$v=19$m=10240,t=10,p=8$2GbVfeHBrTubg30miNYbyQ$521sJfIN6sf+CSJX9sWGhw'


## 使用kaggle下载

```
pip install kaggle
在我的账号里找到kaggle.json文件，放入～.kaggle目录下
然后同意数据集协议，复制下载命令，对数据集进行下载
```


## 启用ssh服务

apt-get install openssh-server

vi /etc/ssh/sshd_config

```python

Port = 22 # 默认是22端口，如果和windows端口冲突或你想换成其他的否则不用动
#ListenAddress 0.0.0.0 # 如果需要指定监听的IP则去除最左侧的井号，并配置对应IP，默认即监听PC所有IP
PermitRootLogin no # 如果你需要用 root 直接登录系统则此处改为 yes
PasswordAuthentication no # 将 no 改为 yes 表示使用帐号密码方式登录

```


然后启动 ssh 服务

service ssh start

如果提示 sshd error: could not load host key 则需要重新生成 key

dpkg-reconfigure openssh-server

查看服务状态

service ssh status

sshd is running  显示此内容则表示启动正常

passwd root 设置下密码

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


# 定时提交
实现对github的定时提交 \
https://my.oschina.net/gcdong/blog/1137849

crontab的使用

http://www.2cto.com/os/201411/348362.html

对crontab的调试

https://blog.csdn.net/biyongyao/article/details/77791238

获取当前时间

https://www.cnblogs.com/zuiyue_jing/p/12557430.html

date不可用的情况

https://stackoverflow.com/questions/58388169/date-command-not-found-in-shell-script

# Ubuntu子系统

LxRunOffline -list

LxRunOffline move -n {version} -d {dir}

设置root密码

sudo passwd root

启动服务与关闭服务<https://zhuanlan.zhihu.com/p/224753478>

# 配置Notedown

```python
pip install https://github.com/mli/notedown/tarball/master
jupyter notebook --NotebookApp.contents_manager_class='notedown.NotedownContentsManager'

jupyter notebook –generate-config 

在配置文件（~/.jupyter/jupyter_notebook_config.py）末尾加入

c.NotebookApp.contents_manager_class = ‘notedown.NotedownContentsManager’

```


# jupyter安装插件

```python
conda install -c conda-forge jupyter_contrib_nbextensions

jupyter contrib nbextension install --user

```

