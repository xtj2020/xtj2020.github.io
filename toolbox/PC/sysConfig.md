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
#更改默认目录
c.NotebookApp.notebook_dir = u'需要默认的路径'
```


### 创建密码

生成密码

jupyter notebook password

导出密码

from notebook.auth import passwd

passwd()

## 开启jupyter服务


jupyter notebook --allow-root




## 使用kaggle下载

```python
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

不能正常启动
sshd: no hostkeys available – exiting

sudo ssh-keygen -A


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


# Ubuntu子系统

LxRunOffline -list

LxRunOffline move -n {version} -d {dir}

设置root密码

sudo passwd

修改密码

sudo passwd root

# 启动服务与关闭服务


Linux子系统（WSL ）是基于 LxssManager 服务运行的。

重启WSL的话只需要将 LxssManager 重启即可。

停止LxssManager服务
net stop LxssManager

启动LxssManager服务
net start LxssManager


在管理员权限的cmd窗口输入 services.msc 打开服务 \
找到LxssManager右键重新启动即可

# 配置Notedown


pip install https://github.com/mli/notedown/tarball/master
jupyter notebook
--NotebookApp.contents_manager_class='notedown.NotedownContentsManager'

jupyter notebook –generate-config

在配置文件（~/.jupyter/jupyter_notebook_config.py）末尾加入

c.NotebookApp.contents_manager_class = ‘notedown.NotedownContentsManager’

# jupyter安装插件

```python
# 卸载
pip uninstall jupyter_contrib_nbextensions
pip uninstall jupyter_nbextensions_configurator

# 安装
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
pip install jupyter_nbextensions_configurator
```


404 GET /static/notebook/js/mathjaxutils.js?v=2021010720231

解决方法：

1. Go to conda envs directory.  e.g. $ cd ~/anaconda3/envs/tf

2. $ vi ./lib/python3.7/site-
packages/jupyter_nbextensions_configurator/static/nbextensions_configurator/render/render.js

3. change 'notebook/js/mathjaxutils' to 'base/js/mathjaxutils'

当出现500错误的时候

conda install nbconvert=5.4.1

如果出现不能自动补全的情况

插件安装Hint

jedi版本过高,需要为0.17

# 查看系统配置

df -h命令来查看磁盘信息， -h 选项为根据大小适当显示

df -hl：查看磁盘剩余空间 \
df -h：查看每个根路径的分区大小 \
du -sh [目录名]：返回该目录的大小 \
du -sm [文件夹]：返回该文件夹总M数 \
du -h [目录名]：查看指定文件夹下的所有文件大小（包含子文件夹）


du 命令用于查看当前目录的总大小： \

-s：对每个Names参数只给出占用的数据块总数。 \
-a：递归地显示指定目录中各文件及子目录中各文件占用的数据块数。若既不指定-s，也不指定-a，则只显示Names中的每一个目录及其中的各子目录所占的磁盘块数。
\
-b：以字节为单位列出磁盘空间使用情况（系统默认以k字节为单位）。 \
-k：以1024字节为单位列出磁盘空间使用情况。 \
-c：最后再加上一个总计（系统默认设置）。 \
-l：计算所有的文件大小，对硬链接文件，则计算多次。 \
-x：跳过在不同文件系统上的目录不予统计。\
-h：以K，M，G为单位，提高信息的可读性。

# pdf转html

pdf2htmlEX
