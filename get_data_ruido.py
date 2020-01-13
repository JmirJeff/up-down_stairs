# conseguir datos de ruido
path1 = 'datos/data_gradas_1.txt'
path2 = 'datos/data_gradas_2.txt'

# cargamos path1
list_data1 = []
with open(path1,'r') as f:
    for i in f:
        list_data1.append(float(i[:-2]))

# cargamos path2
list_data2 = []
with open(path2,'r') as f:
    for i in f:
        list_data2.append(float(i[:-2]))

import random
import matplotlib.pyplot as plt
cuenta = 0
data_ruido = []
while (True):
    try:
        if (cuenta == 110):
            break
        if (random.random()>0.5):
            n = random.randint(0,len(list_data1)-1)
            l = list_data1[n:n+110]
            plt.plot(l)
            plt.show()
        else:
            n = random.randint(0,len(list_data2)-1)
            l = list_data2[n:n+110]
            plt.plot(l)
            plt.show()
        c = input()
        if c=='s':
            data_ruido.append(l)
            cuenta+=1
    except:
        pass

print('datos completos')
print(len(data_ruido))
import pickle
with open('data_none.pickle','wb') as f:
    pickle.dump(data_ruido, f)
