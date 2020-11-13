# 用包来进行调试

import pdb
pdb.set_trace()

break或者b来设置断点
contine或者c来继续执行
在调试过程中打印变量p 变量（pp）
exit与q来推出中止并退出
next或者n来运行下一行，如果是子函数，不会进入子函数
setp运行下一行，如果是子函数，则进入子函数
使用l或者list来显示正在调试的代码位置
debug 在调试的过程中是可以改变变量名的!加变量名
restart重新开启调试
clear清楚所有断点
args(a)打印所有变量
return执行到程序结束
enable/disable启用或者禁止断点

# 使用%pdb进行调试