# 
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',1)#彩色


b=cv2.imread('test.jpg',1)
b=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#BGR轉換RGB
img1=b[0:1000,0:1000]
img2=b[3000:4000,0:1000]

#圖像混和
dst=cv2.addWeighted(img1,0.5,img2,0.5,0)
b[3000:4000,0:1000]=dst



#matplotlib顯示圖案
plt.imshow(b)#(, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()