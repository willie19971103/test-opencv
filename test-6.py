# 剪貼相簿
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',1)#彩色

# img[100,100]==[0,0,0] 將[100,100]轉換為[0,0,0]
print(img.shape)#讀取圖案的大小(4000,6000,3)#3為顏色種數RGB
print(img.size)#像素總數
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#BGR轉換RGB

#roi挖東補西
roi=img1[0:1000,0:2000]##前面的是左上方到左下: 後面是右上到右下
img1[0:1000,4000:6000]=roi  



#matplotlib顯示圖案
plt.imshow(img1)#(, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()