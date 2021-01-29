##幾何變換(放大縮小)
import cv2 
import numpy as np

img=cv2.imread('test2.jpg') 

# 方法一
# 下的 None 本应是出图像的尺寸但是因为后我们置了缩放因子 # 因此为 None 
res=cv2.resize(img,None,fx=0.8,fy=0.8,interpolation=cv2.INTER_CUBIC)

#OR
# 方法二
#  # 呢我们直接置出图像的尺寸所以不用置缩放因子 
height,width=img.shape[:2] 
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
while(1): 
    cv2.imshow('res',res) 
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == 27: 
        break 
