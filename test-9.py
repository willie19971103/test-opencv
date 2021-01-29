#算OPEN運算時間

# 
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',1)#彩色


b=cv2.imread('test.jpg',1)
b=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#BGR轉換RGB

e1 = cv2.getTickCount() #算時間

#建造兩個區塊
img1=b[0:1000,0:1000]
img2=b[3000:4000,0:1000]

#區塊混和
dst=cv2.addWeighted(img1,0.5,img2,0.5,0)##混和比例
b[3000:4000,0:1000]=dst

#算時間e1~e2的時間
e2 = cv2.getTickCount() 
t = (e2 - e1)/cv2.getTickFrequency() 
print(t)#每次都不一樣的時間(有沒有讀到記憶體裡面)


#matplotlib顯示圖案
plt.imshow(b)#(, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()