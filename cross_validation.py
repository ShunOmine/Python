import pandas as pd
from sklearn.utils.testing import all_estimators
from sklearn.model_selection import KFold
import warnings
from sklearn.model_selection import cross_val_score

#アヤメデータの読み込み ---
iris_data = pd.read_csv("iris.csv", encoding="utf-8")

#アヤメデータをラベルと入力データに分離する ---
y = iris_data.loc[:,"Name"]
x = iris_data.loc[:,["SepalLength","SepalWidth","PetalLength","PetalWidth"]]

#classifierのアルゴリズムすべてを取得 ---
warnings.filterwarnings('ignore')
allAlgorithms = all_estimators(type_filter="classifier")

# K分割クロスバリデーション用オブジェクト ---
kfold_cv = KFold(n_splits=5, shuffle=True)

for(name, algorithm) in allAlgorithms:
    #各アルゴリズムのオブジェクトを作成
    clf = algorithm()
    
    #scoreメソッドをもつクラスを対象とする---
    if hasattr(clf,"score"):
        
        #クロスバリデーションを行う---
        scores = cross_val_score(clf, x, y, cv=kfold_cv)
        print(name, "の正解率 =")
        print(scores)