import numpy as np
import cv2

# Create a black image
img=np.zeros((512,512,3), np.uint8)



#畫一條線
# Draw a diagonal blue line with thickness of 5 px
# # Coordinates must be a tuple - (x,y)
# cv2.line(image,(startCoor),(EndCoor),(0,0,0),thickness) 
cv2.line(img,(0,0),(500,500),(255,0,0),5)



#畫一個方塊
# Coordinates must be a tuple - (x,y)
# cv2.rectangle(image,(topLeftCoor),(bottomRightCoor),(0,0,0),thickness)                   #Color is by default black
cv2.rectangle(img,(100,100),(300,300),(0,250,0),-1)

#畫圈圈

# Coordinates must be a tuple - (x,y)
# cv2.circle(image,(CenterCoordinates), radius, (0, 0, 0) ,thickness) 
cv2.circle(img,(200,200), 150, (100,100,100) ,3) 

#一次畫很多條線(多邊形)
# cv2.polylines(image,[coordinates],Boolean(True if closed polygon),(0,0,0))                   #Color is by default black
# 設定多邊形頂點座標
pts = np.array([[100, 100], [200,100], [200,200], [100,200]], np.int32)
# # 將座標轉為 (頂點數量, 1, 2) 的陣列>>>這個不用
# pts = pts.reshape((-1, 1, 2))
# 繪製多邊形
cv2.polylines(img, [pts], True, (255, 255, 0), 3)


#畫橢圓
cv2.ellipse(img,(256,256),(100,50),45,0,360,255,-1)


#寫字
font = cv2.FONT_HERSHEY_COMPLEX
# cv2.putText(image, "text", (Coordinates),font, fontsize, (0, 0, 0),thickness, cv2.LineType)
cv2.putText(img, "test", (350,450),font, 2, (255,255,255),2)

cv2.imshow('window name',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
