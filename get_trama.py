path1 = 'datos/data_gradas_1.txt'
path2 = 'datos/data_gradas_2.txt'

# cargamos path1
list_data = []
with open(path2,'r') as f:
    for i in f:
        list_data.append(i[:-2])

v_found_step = False
v_estable = True
list_steps = []
_list_dat = []
_list_latest_data = []
for i,j in enumerate(list_data):
    print(i,j)
    if (len(_list_latest_data)<15):
        _list_latest_data.append(float(j))
    else:
        _list_latest_data = _list_latest_data[1:]
        _list_latest_data.append(float(j))

    v_estable=True
    for i in _list_latest_data[-10:]:
        if ((i>1)and(i<-1)):
            v_estable = False

    if (v_found_step==False):
        if (((float(j)>=1)or(float(j)<=-1))and(v_estable)):
            v_found_step=True
            _list_dat =  _list_latest_data[:]
    else:
        print(_list_dat)
        _list_dat.append(float(j))
        if (len(_list_dat)==110):
            v_found_step = False
            list_steps.append(_list_dat[:])
            _list_dat.clear()

print(list_steps)
print (len(list_steps))

import matplotlib.pyplot as plt
up = []
down = []
none = []
for i,j in enumerate(list_steps):
    print(i)
    plt.plot(j)
    plt.show()
    d = input()
    if d=='u':
        up.append(i)
    elif d=='d':
        down.append(i)
    elif d=='n':
        none.append(i)

import pickle
dictionary = {'u':up,'d':down,'n':none}
with open('dict_data2.pickle', 'wb') as f:
    pickle.dump(dictionary, f)
with open('list_data2.pickle','wb') as f:
    pickle.dump(list_steps, f)

input('Continuar con segundo procedimiento ...')

dictionary = pickle.load(open('dict_data2.pickle','rb'))
list_steps = pickle.load(open('list_data2.pickle','rb'))

up = dictionary.get('u')
down = dictionary.get('d')
none = dictionary.get('n')
for i,j in enumerate(list_steps):
    if i in up:
        print(i,' up')
        plt.plot(j)
        plt.savefig('imagenes_data_2/up/'+str(i))
        plt.clf()
    elif i in down:
        print(i,' down')
        plt.plot(j)
        plt.savefig('imagenes_data_2/down/'+str(i))
        plt.clf()
    elif i in none:
        print (i,' none')
        plt.plot(j)
        plt.savefig('imagenes_data_2/none/'+str(i))
        plt.clf()
