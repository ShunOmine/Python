import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (500,300))
    #色空間を　HSV　に変換 ---
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
    # HSV を分割する ---
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    v = hsv[:, :, 2]
    #赤っぽい色だけを持つ画像を抽出 ---
    img = np.zeros(h.shape, dtype=np.uint8)
    img[((h < 50)    |  (h > 200)) & (s > 100)] = 255
    
    cv2.imshow('RED Camera', img)
    if cv2.waitKey(1) == 13: break
        
cap.release()
cv2.destroyAllWindows()