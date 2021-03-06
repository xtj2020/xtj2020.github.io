# git的使用

https://www.yiibai.com/git/git_commit.html


## 本地仓

git分为三个仓库：远程仓库、本地仓库、缓存仓库

查看状态：git status \
添加本地仓文件:git add \
提交远程仓库:git push \
git log

先初始化一个本地仓:git init

## 远程仓库

添加远程仓：

git remote add origin git@github.com:xtj2020/laboratory.git

git remote add origin https://github.com/xtj2020/laboratory.git



git pull origin master #从远程仓拉取

git branch –set-upstream-to=origin/master master #设置



git remote 查看所有远程仓库 \
git remote xxx 查看指定远程仓库地址 \
git remote set-url origin 修改远程仓库地址 \
git remote set-url origin git@github.com:xtj2020/laboratory.git


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

## 一个完整的提交过程
git pull

git status

git add -a

git commit -m "描述"

git push


## 自动化提交脚本：

service crond restart

service crond stop

无service服务的时候:

/etc/init.d/cron  top

/etc/init.d/cron start

1、crontab -e

```python
* */2 * * * /bin/bash /Users/xtj2020/notebook/domain_pull.sh
*/5 * * * * /bin/bash /Users/xtj2020/notebook/gitpage_pull.sh
```


2、sh中的编写

```python
source ~/.bash_profile
PATH="/Users/xtj2020/notebook/xtj2020.github.io/"
cd $PATH
currentdate=`/bin/date '+%Y%m%d%H%m'`
/usr/bin/git pull
/usr/bin/git add -A
/usr/bin/git commit -m $currentdate
/usr/bin/git push
/bin/date >>  /Users/xtj2020/notebook/cron.txt
```


3、ps |grep crontab

## win下的自动提交
```bash
@echo off
@title bat execute git auto commit
G:
cd G:\Mirror\Codes\GitHub\xtj2020.github.io
git pull
git add .
git commit -m "Auto commit."
git push
```

在计划任务中选择bat文件


## SSH配置密码
简单的ssh防御 \
https://blog.csdn.net/lailaiquququ11/article/details/83510406

配置ssh

https://docs.github.com/cn/free-pro-team@latest/github/authenticating-to-
github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent


这种方法只是针对局部库
$ git config credential.helper store \

$ git push https://github.com/owner/repo.git

然后输入用户名和密码
Username for 'https://github.com': <USERNAME> \
Password for 'https://USERNAME@github.com': <PASSWORD>

## 版本的回滚

https://blog.csdn.net/ligang2585116/article/details/71094887
