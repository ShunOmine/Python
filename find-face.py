import matplotlib.pyplot as plt
import cv2

# カメラからの入力開始
cap = cv2.VideoCapture(0)

# 動画書き出し用のオブジェクトを生成
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fps = 20.0
size = (640, 360)
writer = cv2.VideoWriter('test.m4v', fmt, fps, size)


while True:
    _, frame = cap.read() #動画を入力

    # カスケードファイルを指定して検出器を作成 --- (*1)
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    # 顔認識を実行 --- (*3)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_list = cascade.detectMultiScale(gray, minSize=(150, 150))

    # 画像を縮小
    frame = cv2.resize(frame, size)

    # 結果を確認
    if len(face_list) == 0:
        print("can't find your face")

    # 認識した部分に印をつける
    # 認識した部分にモザイクをかける
    for (x,y,w,h) in face_list:
        print("顔の座標=", x, y, w, h)
        red = (0, 0, 255)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), red, thickness=20)

    plt.show()

    # 画像を出力
    writer.write(frame)

    # ウィンドウ上にも表示
    cv2.imshow('frame', frame)

    # エンターキーが押されたらループを抜ける
    if cv2.waitKey(1) == 13: break

writer.release()
cap.release()
cv2.destroyAllWindows()
