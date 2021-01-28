**数据的基本类型**

第一种类型是标量scalar，也就是一个单独的字符串string或数字numbers，比如“成都”这个单独的词。

第二种类型是序列sequence，也就是若干个相关的数据按照一定顺序并列在一起，又叫做数组array，或者列表list，比如“成都，重庆”。

第三种类型是映射mapping，也就是一个名/值name/value，即数据有一个名称，还有一个与之相对应的值，这又称作散列hash或字典dictionary，比如“蓉城：成都”。

**jsond
1.并列的数据之间用逗号(,)分隔

2.映射用冒号(:)表示

3.并列数据的集合(数组)用方括号([])表示

4.映射的集合(对象)用大括号({})表示

以上四条规则，就是json格式的所有内容。

JSON建构于两种结构：

（1）“名称/值”对的集合（A collection of name/value pairs）。不同的语言中，它被理解为对象（object），纪录（record），结构（struct），字典（dictionary），哈希表（hash table），有键列表（keyed list），或者关联数组 （associative array）。

（2）值的有序列表（An ordered list of values）。在大部分语言中，它被理解为数组（array）。

**对象**

（名称1：值1，名称2:值2）

**数组**

是值的有序集合

[值1，值2]

值（value）可以是双引号括起来的字符串（string）、数值(number)、true、false、 null、对象（object）或者数组（array）。这些结构可以嵌套。 

### 使用规范及注意事项

1、对象的每个属性都要有双引号

2、数组中可以嵌套对象
