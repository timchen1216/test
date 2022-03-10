import numpy as np
import cv2
from Img2label import img2lable
from Label2numbers import label2number

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)


prediction = []

while True:
    success, img = cap.read()
    label = img2lable(img)
    imgThres = label.preProcessing(img)
    biggest, amount = label.getContours(imgThres)
    cv2.imshow("Input", img)
    
    
    if amount >= 1:
        imgWarped = label.getWarp(img, biggest, amount)
        for i in range(1, amount+1):
            cv2.imshow("Warp"+str(i), imgWarped[i-1])
            number = label2number(imgWarped[i-1])
            predict = number.prediction()
            print('predict :',predict)
            prediction.append(predict)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()  