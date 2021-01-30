#圖像金字塔
import cv2
import numpy as np

img = cv2.imread('test20.jpg')
lower = cv2.pyrDown(img)#取高斯金字塔降階
lower1 = cv2.pyrDown(lower)#降第二層
higher = cv2.pyrUp(lower1)#取高斯生階
higher1 = cv2.pyrUp(higher)#升第二階

while(1):
    cv2.imshow('src', img)
    cv2.imshow('lower', lower)
    cv2.imshow('lower1', lower1)
    cv2.imshow('higher', higher)
    cv2.imshow('higher1', higher1)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
