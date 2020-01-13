# Tratamiento de datos
# lectura
import pickle
dictionary1 = pickle.load(open('dict_data1.pickle','rb'))
list_steps1 = pickle.load(open('list_data1.pickle','rb'))

dictionary2 = pickle.load(open('dict_data2.pickle','rb'))
list_steps2 = pickle.load(open('list_data2.pickle','rb'))

up1 = dictionary1.get('u')
down1 = dictionary1.get('d')
none1 = dictionary1.get('n')

up2 = dictionary2.get('u')
down2 = dictionary2.get('d')
none2 = dictionary2.get('n')

data_up     = []
data_down   = []

for i,j in enumerate(list_steps1):
    if i in up1:
        data_up.append(j)
    elif i in down1:
        data_down.append(j)

for i,j in enumerate(list_steps2):
    if i in up2:
        data_up.append(j)
    elif i in down2:
        data_down.append(j)

data_none = pickle.load(open('data_none.pickle','rb'))
if (__name__=='__main__'):
    print ('Num data up ', len(data_up))
    print ('Num data down ', len(data_down))
    print ('Num data none', len(data_none))

def f_get_data():
    return (data_up,data_down,data_none)
