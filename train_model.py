# entrenamos con los datos
import get_data
(data_up,data_down,data_none) = get_data.f_get_data()

l_up = []
l_down = []
l_none = []
for i in data_up:
    l_up.append('up')
for i in data_down:
    l_down.append('down')
for i in data_none:
    l_none.append('none')

#separamos los datos
import numpy as np
from sklearn.model_selection import train_test_split

data_x_full = data_up + data_down + data_none
data_y_full = l_up + l_down + l_none

X_train, X_test, y_train, y_test = train_test_split(data_x_full,data_y_full,test_size = 0.3)

print(len(X_train),len(X_test),len(y_train),len(y_test))

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(activation='relu',solver='sgd',alpha=0.0001,hidden_layer_sizes=(5,3),learning_rate='adaptive',learning_rate_init=0.001,max_iter=5000)

print('entrenando')
clf.fit(X_train, y_train)
print('entrenado')

print (clf.score(X_train, y_train))
print (clf.score(X_test,y_test))

import numpy

def relu(x):
    return np.maximum(x,0.)

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

import pickle
with open('clf.pickle','wb') as f:
    pickle.dump(clf, f)
