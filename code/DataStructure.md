https://leetcode-cn.com/problemset/algorithms/?difficulty=%E7%AE%80%E5%8D%95

1. 两数之和 

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

```{.python .input  n=3}
hashtable = dict()
hashtable[11]
```

```{.json .output n=3}
[
 {
  "ename": "KeyError",
  "evalue": "11",
  "output_type": "error",
  "traceback": [
   "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
   "\u001b[0;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
   "\u001b[0;32m<ipython-input-3-d11de8732b95>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mhashtable\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mhashtable\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m11\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
   "\u001b[0;31mKeyError\u001b[0m: 11"
  ]
 }
]
```
