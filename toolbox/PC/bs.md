### 将文档传入Beautiful soup

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