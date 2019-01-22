import cv2
import numpy as np
from mosaic import mosaic as mosaic

cap = cv2.VideoCapture(0)
img_last = None #前回の画像を記憶する変数
green = (0, 255, 0)
fmt = cv2.VideoWriter_fourcc('m','p','4','v')
fps = 20.0
size = (640, 360)
writer = cv2.VideoWriter('diff_camera.m4v', fmt, fps, size) #---

while True:
    #画像を取得
    _, frame = cap.read()
    frame = cv2.resize(frame, size)
    writer.write(frame)
    #白黒画像に変換 ---
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9, 9), 0)
    img_b = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]
    #差分を確認する ---
    if img_last is None:
        img_last = img_b
        continue
    frame_diff = cv2.absdiff(img_last, img_b) #---
    cnts = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
    #差分があった点を画面に書く ---
    for pt in cnts:
        x, y, w, h = cv2.boundingRect(pt)
        if w < 30: continue #小さな変更点は無視 ---
        cv2.rectangle(frame, (x, y), (x+w, y+h), green, 2)
        
    #今回のフレームを保存 ---
    img_last = img_b
    #画面に表示 ---
    cv2.imshow("Diff Camera", frame)
    cv2.imshow("diff data", frame_diff)
    if cv2.waitKey(1) == 13: break

writer.release()
cap.release()
cv2.destroyAllWindows()