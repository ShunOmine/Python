import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import glob

#Unicodeのコードポイント頻度測定
def count_codePoint(str):
    counter = np.zeros(65535)
    
    for i in range(len(str)):
        code_point = ord(str[i])
        if code_point > 65535 :
            continue
            
        counter[code_point] += 1
        
    counter = counter/len(str)
    return counter

#学習データの準備
index = 0
x_train = []
y_train = []
for file in glob.glob('./Python/train/*.txt'):
    #言語情報を取得し、ラベルに設定 ---
    y_train.append(file[15:17])
    
    #ファイル内の文字列を連結後、Unicodeのコードポイントの頻度を測定し、入力データに設定 ---
    file_str = ''
    for line in open(file, 'r'):
        file_str = file_str + line
    x_train.append(count_codePoint(file_str))
    
#学習する
clf = GaussianNB()
clf.fit(x_train, y_train)

#評価データの準備 ---
index = 0
x_test = []
y_test = []
for line in glob.glob('./Python/test/*.txt'):
    #言語情報を取得し、ラベルに設定
    y_test.append(file[14:16])
    
    #ファイル内の文字列を連結後、Unicodeのコードポイントの頻度を測定し、入力データに設定 ---
    file_str = ''
    for line in open(file, 'r'):
        file_str = file_str + line
    x_test.append(count_codePoint(file_str))
    
#評価する
y_pred = clf.predict(x_test)
print(y_pred)
print("正解率 = ", accuracy_score(y_test, y_pred))