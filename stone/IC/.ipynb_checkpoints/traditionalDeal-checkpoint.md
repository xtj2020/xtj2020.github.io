图像格式的转化

```python

image = cv2.imread("/home/xtu_conda/xtjdata/RF2021/Training_Set/Training/1741.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

```

绘制hist图，hist()第一个返回值是统计各个区间的频数，第二个返回值是bins，即区间，可以进行绘制看

plt.hist(image.ravel(), 256)

使用THRESH_OTSU 方法进行阈值分割

```python

ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  #方法选择为THRESH_OTSU 

```
