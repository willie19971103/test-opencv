import numpy as np
import cv2
from matplotlib import pyplot as plt
# img = cv2.imread('test.jpg',cv2.IMREAD_COLOR)#彩色
img = cv2.imread('test.jpg',1)#彩色
# img = cv2.imread('test.jpg',0)#黑白
# img = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)#黑白色
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#BGR轉換RGB

# print(img)#確認資訊在不在

#cv2顯示圖案
# cv2.namedWindow('test',cv2.WINDOW_NORMAL)#可調整視窗大小
# cv2.imshow('test',img)#看圖
# cv2.imwrite('test1.jpg',img)#寫入儲存檔案
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#matplotlib顯示圖案
plt.imshow(img1)#(, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()