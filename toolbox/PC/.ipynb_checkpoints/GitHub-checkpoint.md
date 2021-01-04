# git的使用

https://www.yiibai.com/git/git_commit.html

git分为三个仓库：远程仓库、本地仓库、缓存仓库

查看状态：git status \
添加本地仓文件:git add \
提交远程仓库:git push 
git log

### 本地仓

先初始化一个本地仓:git init

然后用本地仓与远程仓进行关联：

git remote add origin git@github.com:xtj2020/laboratory.git

## 新建一个远程仓库

git remote 查看所有远程仓库 \
git remote xxx 查看指定远程仓库地址 \
git remote set-url origin 你新的远程仓库地址 \
git@github.com:YotrolZ/helloTest.git


git remote set-url origin git@github.com:xtj2020/laboratory.git






## 定时提交
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

## 一个完整的过程
git pull

git status

git add -a 

git commit -m "描述"

git push

## 不用每次输密码

git remote -v

修改为https的方式：

git remote set-url origin https://github.com/xmanrui/autoftp.git

修改为ssh的方式:

git remote set-url origin git@github.com:xmanrui/timerecord.git

git config --global credential.helper store

 --global  表示全局的，即当前用户都有效，该配置会出现在 ~/.gitconfig 文件中
 
局部是只对当前仓库起效的，它的配置信息会在当前仓库根目录/.git/config文件下
 
 

查看配置列表 \
git config --list

git config --global user.name "maxsu" \
git config --global user.email maxsu@yiibai.com

## SSH配置密码
简单的ssh防御 \
https://blog.csdn.net/lailaiquququ11/article/details/83510406

配置ssh

https://docs.github.com/cn/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent


这种方法只是针对局部库
$ git config credential.helper store \

$ git push https://github.com/owner/repo.git

然后输入用户名和密码
Username for 'https://github.com': <USERNAME> \
Password for 'https://USERNAME@github.com': <PASSWORD>

## 版本的回滚
    
https://blog.csdn.net/ligang2585116/article/details/71094887    
