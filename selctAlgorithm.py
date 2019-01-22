import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
from sklearn.utils.testing import all_estimators

#アヤメデータの読み込み ---
iris_data = pd.read_csv("iris.csv", encoding="utf-8")

#アヤメデータをラベルと入力データに分離する ---
y = iris_data.loc[:,"Name"]
x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

#学習用とテスト用に分離する ---
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, train_size = 0.8, shuffle = True)

#classifierのアルゴリズムすべてを取得する ---
allAlgorithms = all_estimators(type_filter="classifier")

for(name, algorithm) in allAlgorithms:
    clf = algorithm()
    
    #学習して、評価する ---
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)