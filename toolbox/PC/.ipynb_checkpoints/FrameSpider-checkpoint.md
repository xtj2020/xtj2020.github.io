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

### 正则表达式

#### 1、匹配

## 匹配

元字符：. ^ $  * + ? { } [ ] ( ) \ |

[ ] : 指定字符类，字符类中元字符不生效（特殊情况^开头作为非出现），是或的含义。

\ ：1、跟字符指示特殊序列；2、转义所有元字符，使得能够匹配元字符本身

特殊序列：

| 字符 |            用法            |
| ---- | :------------------------: |
| .    | 匹配除换行符之外的任意字符 |
| \d   |            数字            |
| \D   |           非数字           |
| \s   |            空白            |
| \S   |           非空白           |
| \w   |            单词            |
| \W   |           非单词           |

\d\d\d会精准匹配三位数，等价于{3}

\s可以使用重复

[^abc] 将匹配除abc的单个字符

## 重复

*匹配零次或多次，贪婪的，尽可能多的匹配，不匹配退回进行匹配。

+匹配一次或多次，至少一次

？匹配一次或零次

{m,n}至少m次，至多n次

## 零宽度

\b 位于字边界

｜或 “or”具备非常低的优先级

^只会在字符串的开头匹配，即使设置MULTILINE也在字符串中每个换行符后进行匹配

$匹配行的末尾

\\a起始

\\b 前面是一个单词，后面是一个非单词

\A

\Z

## 捕获分组

( )只会捕获（）内的内容

嵌套的捕获组，按顺序进行提取

可以在捕获组后加？这样不会影响前面的捕获组

## 非捕获

(? : ...) 只做匹配，不做捕获

（？=...）前向断言 只匹配对的

（? ! ...）后向断言 只匹配不对的

#### 2、应用编译	

## 编译与应用

compile

math 只匹配字符串的开始

search 对整个字符串进行搜索

findall 获取所有匹配的字符串，返回一个列表

finditer 返回一个迭代器

## 编译标志

A

S

I

L

M

X

####  3、修改	

split() 将字符串拆分为一个列表

```
import re
text = 'a,b,c,,,d'
reobj = re.compile（'[,]+'）
reobj.spilt(text)
#等价于
re.spilt('[,]+',text)
```


sub() 找到所有子字符，并进行替换
sub('具体模式'，源字符串)，返回值是一个字符串

subn() 会返回新字符串和替换次数

# 代码基准

```
[0-9][0-9]可以实现两位数字的匹配，用[0-99]会出现匹配单位数
```


# 存储

存入数据库或者相关文本工具

# 框架

scrapy框架

# Beautiful soup

## 将文档传入Beautiful soup

### 对象种类

#### Tag：

两个属性name和attributes

* name

每个tag都有自己的名字,通过 `.name` 来获取:
如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档

* attributes

 

#### NavigableString

Beautiful Soup用 `NavigableString` 类来包装tag中的字符串

一个 `NavigableString` 字符串与Python中的Unicode字符串相同,并且还支持包含在 [遍历文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id18) 和 [搜索文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id27) 中的一些特性. 通过 `unicode()` 方法可以直接将 `NavigableString` 对象转换成Unicode字符串

tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 [replace_with()](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#replace-with) 方法



#### BeautifulSoup

`BeautifulSoup` 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 `Tag` 对象,它支持 [遍历文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id18) 和 [搜索文档树](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id27) 中描述的大部分的方法.

因为 `BeautifulSoup` 对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 `.name` 属性是很方便的,所以 `BeautifulSoup` 对象包含了一个值为 “[document]” 的特殊属性 `.name`

2.2.4 Comment





### 遍历文档树

#### 子节点

利用tag的名字

#### 父节点

.parent

.parents

#### 兄弟节点

在文档树中,使用 `.next_sibling` 和 `.previous_sibling` 属性来查询兄弟节点

#### 回退与前进

.next_element 和 .previous_element

### 搜索文档树

#### 过滤器

过滤器只能**作为搜索文档的参数**,或者说应该叫参数类型更为贴切,原文中用了 `filter` 因此翻译为过滤器

* 最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容，

```
soup.find_all('b')
```


* 如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 `match()` 来匹配内容.

```
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
```


* 如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.

```
soup.find_all(["a", "b"])
```


####  find_all()

find_all( name , attrs , recursive , string , **kwargs )





###  修改文档树

### 输出

### 解析器

### 编码

###  其他
