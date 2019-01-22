import cv2
import numpy as np

#web カメラから入力を開始
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (500,300))
    #青と緑の成分を0に(Numpy　のインデックスを利用）---
    frame[:, :, 0] = 0 #青要素を0
    frame[:, :, 1] = 0 #緑要素を0
    
    cv2.imshow('RED Camera', frame)
    if cv2.waitKey(1) == 13: break
        
cap.release()
cv2.destroyAllWindows()