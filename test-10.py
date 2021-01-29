##轉換顏色空間
import cv2 

#顏色種類列表
flags=[i for i in dir(cv2) if i.startswith('COLOR_')] 
print(flags)
print(len(flags))

#
cv2.cvtColor(img,cv2.COLOR_BAYER_RBG2HSV)
