from sklearn import datasets, svm
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score

clf = joblib.load('iris.pkl')

iris = datasets.load_iris()

pre = clf.predict(iris.data)

print(accuracy_score(iris.target, pre))