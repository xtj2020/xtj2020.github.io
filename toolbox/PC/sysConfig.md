# 系统配置(system)

## jpyter系统配置

```python
#设置密码与指定端口
c.NotebookApp.password=u'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
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

```
argon2:$argon2id$v=19$m=10240,t=10,p=8$CTE4Cy82xEK+UI3IEZwd5A$QQp58PNCbEfmJABqe4Jf0A
```

```
pip install kaggle
在我的账号里找到kaggle.json文件，放入～.kaggle目录下
```

36号机密码（存疑）

```
sha1:dc17e5844fdc:81d5f49b2ed73c5f7ebc0300b2e30b1f395e5882 
```

