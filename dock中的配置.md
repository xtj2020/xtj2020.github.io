None
# 使用的dock镜像

https://github.com/jupyter/docker-stacks

# 安装编辑器

apt-get update

apt-get -y install vim

# priority.j2

Jupyter上无法保存md文件，报错：Unexpected error while saving file xxx/README.md display_priority.j2

从标亮出看到问题是jinja2.exceptions.TemplateNotFound: display_priority.j2，然后报错的文件在c:\programdata\anaconda3\envs\py37\share\jupyter\nbconvert\templates\compatibility\display_priority.tpl

![img](https://xtj2020.top/webimg/priorityj2.png)

改成base/display_priority.j2

# 拷贝文件

docker cp docker文件路径 本机路径

# 保存容器

docker commit 

docker commit -m "描述" ID号

docker tag 0bc42f7ff218 webapp:1.0

docker commit -m "upgrade" webapp webapp：2.0

# 执行命令

docker ps -a

docker exec -it mynginx /bin/sh

docker exec -u root -it mynginx /bin/sh
