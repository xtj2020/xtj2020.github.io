# 对文件夹的处理

```python
## 列出输入目录中文件的个数
def lenDirFile(img_path):
    return len(os.listdir(img_path))

## 移除指定路径下的文件
def removeDirFile(img_path):
    try:
        shutil.rmtree(img_path)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(img_path)
    print("\n 文件列表：",os.listdir(img_path),"\n 文件个数：",len(os.listdir(img_path)))
```


# 迭代器操作

```python
def get_length(generator):
    if hasattr(generator,"__len__"):
        return len(generator)
    else:
        return sum(1 for _ in generator)
```    

# 对图像的处理
```python    
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



# 双点裁切
def crop_pic(imgPath,edge_size):
#         imgPath = "../xtjdata/RF2021/Training_Set/Training/1751.png"
    img = getPixel(imgPath)
    print("原图片的尺寸：",img.shape)
    Red = img[:, :, 0] *0.2126
    Green = img[:, :, 1] *0.7152
    Blue = img[:, :, 2] * 0.0772
    new_img = Red+Green+Blue
    c = np.where(new_img>edge_size)
#     print(c)
    left = np.min(c[0])
    right = np.max(c[0])
    mid = int((left+right)/2)
    low = np.min(c[1]) #这条边有不对的点
    while new_img[mid][low] >= new_img[mid][low+1] or new_img[mid+50][low] >= new_img[mid+50][low+1]:
        low += 1 
    top = np.max(c[1])
    show_img = img[left+1:right-1,low:top,:]
    print("剪裁后尺寸：",show_img.shape)
    shape_list.append(show_img.shape)
    return show_img,show_img.shape
#     plt.figure()
#     plt.imshow(show_img)
#     plt.show()

```


```python
class person:
    """
    输入id，df作为一个全局变量
    是否健康health=Ture,若False，能够获取病人患病总数nums_disease,种类数types_Edisease,中文名type_Cdisease
    返回图片路径person_imgPath，返回图片的像素imgPixel
    """
    def __init__(self,id):
        self.id = id
        self.imgPath = "../xtjdata/RF2021/Training_Set/Training/"+str(person_id)+".png"
                
    def get_disease(self):
        types_Edisease = []
        for i in values_list:
            if df[i][self.id-1] == 1:
                dieseas_list.append(i)
        return dieseas_list
    
    def getPixel(id):
        img_str = str(id)+".png"
        imgPath = os.path.join("../xtjdata/RF2021/Training_Set/Training/",img_str)
        img=Image.open(imgPath)
        array_img = np.array(img)
        img.close()
        return array_img
    
#原始的标签表
label_df=pd.read_csv("/home/xtu_conda/xtjdata/RF2021/Training_Set/RFMiD_Training_Labels.csv")
# 缩写、中英对照表
name_df=pd.read_csv("chinese_name.csv")

def get_sumLabel_df():
    sumLabel_df = label_df.copy()
    sumLabel_df["sumLabel"]=''
    sumLabel_df["sumLabel"]=label_df.iloc[:,2:].sum(axis=1)
    return sumLabel_df
sumLabel_df = get_sumLabel_df()



def statistic_pixel():
    shape_list = []
    id_list = []
    for i in trange(1920):
        i +=1
        id_list.append(i)
        shape_list.append(getPixel(i).shape) 
    return id_list,shape_list 

#获取多重患病的id
def getID_multiplyDisease(n):
    all_id = []
    for id in df["ID"]:
        if df["sumLabel"][id-1] == n:
            all_id.append(id)
        else:
            pass
    print("总共：",len(all_id))
    return all_id

#返回所有疾病的患病个数
def disease_nums():
    nums_person = []
    values_list = df[""]
    for i in values_list:
        nums_person.append(df[i].value_counts()[1])

    a = zip(values_list,nums_person)
    disesase = [x  for x in a]
    sorted(disesase, key=lambda x:x[1],reverse=True) 
    return disesase


def get_AlldiseaseAb():
    AlldiseaseName = label_df.columns.values[2:]
    return AlldiseaseName

def get_countsLable():
    df["sumLabel"].value_counts()
```

