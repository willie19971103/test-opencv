# RGB混色
import numpy as np
import cv2
from matplotlib import pyplot as plt


i = cv2.imread('test.jpg',1)
# i[:,:,0]=0 #紅色消除
# i[:,:,1]=0 #綠色消除
# i[:,:,2]=0 #藍色消除
i[100:200,100:200,0]=0
i[300:500,600:800,1]=0
i[500:600,300:500,2]=0


#matplotlib顯示圖案
plt.imshow(i)#(, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()