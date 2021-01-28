import numpy as np

# ovid套件 :讀取鏡頭

# owvid套件:讀取並寫入
#Import only if not previously imported
import cv2
# Create a Video Reader Object.
cap = cv2.VideoCapture(VideoToRead)#抓哪顆鏡頭
if cap.isOpened() == False:
    print("Error in opening video stream or file")
#Define the codec for the Video
fourcc = cv2.VideoWriter_fourcc("Fourcc Codec Eg-XVID")#預設裡面放*XVID
#Create Video Writer Object
writer = cv2.VideoWriter('Video Writing Address',fourcc, fps value, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        writer.write(frame)
        cv2.imshow("Frame",frame)
        # Exit on pressing esc
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
#關掉使用的物件
cap.release()
writer.release()
cv2.destroyAllWindows()