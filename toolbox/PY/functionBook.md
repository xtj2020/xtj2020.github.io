```{.python .input  n=6}
```python

## 获取迭代器的长## 获取迭代器的长度
def get_length(generator):
    if hasattr(generator,"__len__"):
        return len(generator)
    else:
        return sum(1 for _ in generator)
    
    
##图像的去噪 
def cut_pic(read_file): 
    img = cv2.imread(read_file)   
    h, w, _ = img.shape

    GrayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #图片灰度化处理
    ret,binary = cv2.threshold(GrayImage,15,255,cv2.THRESH_BINARY) #图片二值化,灰度值大于40赋值255，反之0
    threshold = 10   #噪点阈值
    contours,hierarch=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    # 直接填充二值图
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])          #计算轮廓所占面积
        if area < threshold:                         #将area小于阈值区域填充背景色
            cv2.drawContours(binary, [contours[i]],-1, 0, thickness=-1)     #原始图片背景0
            continue

    #     print(binary.shape,end=' ')
    #找到填充后轮廓的边界
    #找到所有目标点 横坐标、纵坐标
    edges_x,edges_y = np.where(binary==255)

    top = min(edges_x)                 #上边界
    bottom = max(edges_x)              #下边界
    height=  bottom  - top               #高度

    left = min(edges_y)             #底部
    right = max(edges_y)                #左边界
    width = right - left                #右边界
    #返回剪切图
    return img[top:top+height,left:left+width]
def smaller_pic(i):
    img = "/home/xtu_conda/xtjdata/RF2021//Training_Set/classedPiexl/1424/"+str(i)
    new_path = "/home/xtu_conda/xtjdata/small-RF/originData/"+str(i)
    img_src = cv2.imread(img)
    img_result1 = cv2.resize(img_src, (0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_LINEAR)
    shape_list.append(img_result1.shape)
    image = Image.fromarray(cv2.cvtColor(img_result1,cv2.COLOR_BGR2RGB))    
    image.save(new_path)
    return shape_list
```
```

```{.json .output n=6}
[
 {
  "ename": "SyntaxError",
  "evalue": "invalid syntax (<ipython-input-6-f38e232858e8>, line 1)",
  "output_type": "error",
  "traceback": [
   "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-6-f38e232858e8>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    ```python\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
  ]
 }
]
```

```{.python .input}
# %load functionBook.py
## 获取迭代器的长## 获取迭代器的长度
def get_length(generator):
    if hasattr(generator,"__len__"):
        return len(generator)
    else:
        return sum(1 for _ in generator)
    
    
##图像的去噪 
def cut_pic(read_file): 
    img = cv2.imread(read_file)   
    h, w, _ = img.shape

    GrayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #图片灰度化处理
    ret,binary = cv2.threshold(GrayImage,15,255,cv2.THRESH_BINARY) #图片二值化,灰度值大于40赋值255，反之0
    threshold = 10   #噪点阈值
    contours,hierarch=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    # 直接填充二值图
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])          #计算轮廓所占面积
        if area < threshold:                         #将area小于阈值区域填充背景色
            cv2.drawContours(binary, [contours[i]],-1, 0, thickness=-1)     #原始图片背景0
            continue

    #     print(binary.shape,end=' ')
    #找到填充后轮廓的边界
    #找到所有目标点 横坐标、纵坐标
    edges_x,edges_y = np.where(binary==255)

    top = min(edges_x)                 #上边界
    bottom = max(edges_x)              #下边界
    height=  bottom  - top               #高度

    left = min(edges_y)             #底部
    right = max(edges_y)                #左边界
    width = right - left                #右边界
    #返回剪切图
    return img[top:top+height,left:left+width]
def smaller_pic(i):
    img = "/home/xtu_conda/xtjdata/RF2021//Training_Set/classedPiexl/1424/"+str(i)
    new_path = "/home/xtu_conda/xtjdata/small-RF/originData/"+str(i)
    img_src = cv2.imread(img)
    img_result1 = cv2.resize(img_src, (0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_LINEAR)
    shape_list.append(img_result1.shape)
    image = Image.fromarray(cv2.cvtColor(img_result1,cv2.COLOR_BGR2RGB))    
    image.save(new_path)
    return shape_list
```
