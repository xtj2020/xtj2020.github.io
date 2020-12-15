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