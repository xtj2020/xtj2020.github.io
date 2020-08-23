返回的是一个silde对象，使用get_tile获取RGB Image图像

```python

import openslide
import matplotlib.pyplot as plt
img_path = '../input/prostate-cancer-grade-assessment/train_label_masks/00c15b23b30a5ba061358d9641118904_mask.tiff'
slide1 = openslide.OpenSlide(img_path)
simg = slide1.get_thumbnail((206,400))
plt.imshow(simg)


```

```python
from openslide.deepzoom import DeepZoomGenerator
gen_img = DeepZoomGenerator(slide_img,tile_size=1023,overlap=1,limit_bounds=False)
gen_img_mask = DeepZoomGenerator(slide_img_mask,tile_size=1023,overlap=1,limit_bounds=False)

gen_img.level_tiles

img_a = gen_img.get_tile(11,(0,0))
img_b = gen_img_mask.get_tile(11,(0,0))
plt.imshow(img_a)
plt.show()
plt.imshow(img_b)
plt.show()

I_img = slide_img.get_thumbnail((206,400))
I_img_mask = slide_img_mask.get_thumbnail((206,400))
plt.imshow(I_img)
plt.show()
plt.imshow(I_img_mask)
plt.show()

a = slide1.read_region((0,0),0,(1024,1024))
type(a)

```

