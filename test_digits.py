import matplotlib.pyplot as plt

#手書きデータの読み込み ---
from sklearn import datasets
digits = datasets.load_digits()

#15個連続で出力する ---
for i in range(15):
    plt.subplot(3, 5, i + 1)
    plt.axis("off")
    plt.title(str(digits.target[i]))
    plt.imshow(digits.images[i], cmap="gray")
    
plt.show()