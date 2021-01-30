# 抓輪廓
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('IMG.jpg')#匯入檔案
img1 = img.copy() #複製一份檔案
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#轉換色域

blurred = cv2.GaussianBlur(imgray, (11, 11), 0) #高斯濾鏡


edges = cv2.Canny(blurred, 150, 200) #Canny偵測邊界的MAX MIN



contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#找到邊界
print(len(contours))
draw = cv2.drawContours(img1, contours, -1, (0, 255, 0), 5)#畫出所有輪廓


#作圖
plt.subplot(131), plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(132), plt.imshow(edges,cmap='gray'), plt.title('Edge Image')
plt.subplot(133), plt.imshow(cv2.cvtColor(draw,cv2.COLOR_BGR2RGB)), plt.title('contour Image')

plt.show()




