# 爬取

## 基本抓取

常用库：requests、urllib2、httplib2

```python
import requests
respose = requests.get(url1)
content = requests.get(url).content 返回一个html二进制文件，能够自动进行转码
pring(repose.headers)
```

带查询字段的
例如使用bing搜索，链接为：

```
https://cn.bing.com/search?q=%E7%AE%80%E5%8D%95&PC=U316&FORM=CHROMN]https://cn.bing.com/search?q=简单&PC=U316&FORM=CHROMN)
```

？分割url和传输数据，多个参数用&连接

```
data = {'q':'搜索','PC':'U316','form':'CHROMN'}
#get会自动用=替换掉：
response = requests.get(url='https://cn.bing.com/search?',params = data)

```



## 反爬虫

### 模拟登录

requests.post(url = url1,data=data)
post用于用户名密码登陆 

### 使用cookie

使用requests.session()创建会话，可以记录cookies

**在验证码之后拿到cookies**

### 使用代理



断线重连

多线程

Ajax

验证码



# 分析

正则表达式

[表达式]: rk.md

beautiful soup

lxml



# 存储

存入数据库或者相关文本工具

# 框架

scrapy框架

