from sklearn import datasets
import keras
from keras.models import load_model
from keras.utils.np_utils import to_categorical

iris = datasets.load_iris()
in_size = 4
nb_classes = 3

x = iris.data
y = to_categorical(iris.target, nb_classes)

model = load_model('iris_model.h5')

model.load_weights('iris_weights.h5')

score = model.evaluate(x, y, verbose=1)
print("正解率 = ", score[1])