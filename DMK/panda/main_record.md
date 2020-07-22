# 所需要的库

```python
import openslide
from matplotlib import pyplot as plt
from openslide.deepzoom import DeepZoomGenerator
import numpy as np
import pandas as pd 
import cv2 as cv
import skimage.io 
from PIL import Image 
from tqdm.notebook import tqdm
from scipy import misc
import os.path
import matplotlib
```



# 导入图像

## cv2尝试

cv2.imread(' ',1) 不能将图片读取进去

弄清cv2.add函数的使用

```python
import cv2
import numpy as np
img = cv2.imread('../input/prostate-cancer-grade-assessment/train_images/0005f7aaab2800f6170c399693a96917.tiff',1)
# 创建掩膜
maskName = '../input/prostate-cancer-grade-assessment/train_label_masks/0005f7aaab2800f6170c399693a96917_mask.tiff'
mask = cv2.imread(maskName, cv2.IMREAD_GRAYSCALE)
res = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint16), mask=mask)

#保存图片
print(img)
```

```python
def add_mask2image_binary(images_path, masks_path, masked_path):
# Add binary masks to images
    for img_item in os.listdir(images_path):
        print(img_item)
        img_path = os.path.join(images_path, img_item)
        img = cv2.imread(img_path)
        mask_path = os.path.join(masks_path, img_item[:-4]+'.png')  # mask是.png格式的，image是.jpg格式的
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)  # 将彩色mask以二值图像形式读取
        masked = cv2.add(img, np.zeros(np.shape(img), dtype=np.uint8), mask=mask)  #将image的相素值和mask像素值相加得到结果
        cv2.imwrite(os.path.join(masked_path, img_item), masked)
images_path = '/home/xinan/cat_test/image/'
masks_path = '/home/xinan/cat_test/catmask/'
masked_path = '/home/xinan/cat_test/masked/'
add_mask2image_binary(images_path, masks_path, masked_path)
```

## 使用opensilde读取

成功读取并获得图像原始尺寸大小

```python
import openslide
import matplotlib.pyplot as plt
img_path = '../input/prostate-cancer-grade-assessment/train_label_masks/00c15b23b30a5ba061358d9641118904_mask.tiff'
slide1 = openslide.OpenSlide(img_path)
print(slide1.dimensions)
```

## 使用skimage读取

```python
skimage.io.MultiImage(path)
```

## 时间效率

skiage读取更快

# 图像的缩放

## 时间效率

```python
%timeit img = biopsy.get_thumbnail(size=(512, 512))
%timeit out = resize(biopsy2[-1], (512, 512))
%timeit out = cv2.resize(biopsy2[-1], (512, 512))
%timeit out = Image.fromarray(biopsy2[-1]).resize((512, 512))
```

## 正方形缩放

## 串联缩放

# 文件夹处理

```python
for img_item in os.listdir('../input/prostate-cancer-grade-assessment/train_images'):
    print(img_item)
```

```
out = cv2.resize(biopsy2[-1], (512, 512))

%timeit Image.fromarray(out).save(img_id+'.png')
%timeit cv2.imwrite(img_id+'.png', out)
```