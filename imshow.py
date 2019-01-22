%matplotlib inline

#ダウンロードした画像を画面に表示 ---
import matplotlib.pyplot as plt
import cv2
img = cv2.imread("test.png")
plt.axis("off")
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()