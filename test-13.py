##圖案轉換點
import cv2 
import numpy as np 
from matplotlib import pyplot as plt

#轉換點格式
pts1 = np.float32([[0,0],[0,0],[0,0],[0,0]]) #預設4個點為0

i=0
#定義滑鼠要幹嘛
def savexy(event,x,y,flags,param):
    global pst1
    global i
    if event==cv2.EVENT_LBUTTONDBLCLK:
        print(x,y) #可印在程式裡面
        #cv2.circle(img,(x,y), 3, (0,0,0) ,3)也可以換畫點點
        pts1[i]=[x,y]#按下滑鼠會將原本預設的數值更改
        i+=1

img=cv2.imread('test2.jpg')
rows,cols,ch=img.shape

#第二條線為對齊線
pts2 = np.float32([[0,0],[400,0],[0,400],[400,400]])#向中間線對齊


#先開一張圖image
cv2.namedWindow('image')
cv2.setMouseCallback('image',savexy)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27 or i>3:
        break
cv2.destroyAllWindows()

M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(300,300))
dst1 = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst1), plt.title('Output')
plt.show()

