"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
import random, string
import timeit


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


def d_addel():
    for i in range(1000):
        d[i] = i

def od_addel():
    for i in range(1000):
        od[i] = i

def od_popfirst():
    for i in range(1000):
        od.popitem(last = False)

def d_popfirst():
    for i in range(1000):
        d.pop(list(d.keys())[0])

def od_poplast():
    for i in range(1000):
        od.popitem(last = True)

def d_poplast():
    for i in range(1000):
        d.popitem()


def od_movetoend():
    for i in range(1000):
        od.move_to_end(list(od.keys())[0],last = True)

def d_movetoend():
    for i in range(1000):
        kbuf = list(d.keys())[0]
        buf = d.pop(kbuf)
        d[kbuf] = buf

def od_update():
    od.update(tempdict)

def d_update():
    d.update(tempdict)


def d_randomacess():
    return d[list(d.keys())[random.randint(0,999)]]

def od_randomacess():
    return od[list(od.keys())[random.randint(0, 999)]]

def d_randomacess():
    return d[list(d.keys())[random.randint(0,999)]]

def od_randomacess():
    return od[list(od.keys())[random.randint(0, 999)]]


od = OrderedDict()
d = {}
k = []
v = []
for i in range(1000):
    k.append(randomword(10))
    v.append(random.randint(-10000000000,10000000000))

print("dict add element: ", timeit.timeit(d_addel, number=1000)) #обычный быстрее
print("ordereddict add element: ", timeit.timeit(od_addel, number=1000)) #


od = OrderedDict()
d = {}
for i in range(1000):
    od[k[i]] = v[i]
    d[k[i]] = v[i]
print("dict pop last element: ", timeit.timeit(d_poplast, number=1)) # обычный быстрее
print("ordereddict pop last element: ", timeit.timeit(od_poplast, number=1)) #

for i in range(1000):
    od[k[i]] = v[i]
    d[k[i]] = v[i]
print("dict pop first element: ", timeit.timeit(d_popfirst, number=1)) # ordereddict быстрее
print("ordereddict pop first element: ", timeit.timeit(od_popfirst, number=1))


od = OrderedDict({'1':1,'-2':-2,'2':122})
d = {'1':1,'-2':-2,'2':122}
tempdict = {}
for i in range(1000):
    tempdict[k[i]] = v[i]
print("dict update: ", timeit.timeit(d_update, number=1)) # обычный быстрее
print("ordereddict update: ", timeit.timeit(od_update, number=1))


od = OrderedDict()
d = {}
tempdict = {}
for i in range(1000):
    od[k[i]] = v[i]
    d[k[i]] = v[i]
print("dict move to end: ", timeit.timeit(d_movetoend, number=1)) # обычный быстрее
print("ordereddict move to end: ", timeit.timeit(od_movetoend, number=1)) #

od = OrderedDict()
d = {}
tempdict = {}
for i in range(1000):
    od[k[i]] = v[i]
    d[k[i]] = v[i]
print("dict move to end: ", timeit.timeit(d_randomacess, number=1000)) # обычный быстрее
print("ordereddict move to end: ", timeit.timeit(od_randomacess, number=1000))

"""
В большинстве случаев обычный массив быстрее, ordereddict следует использовать только если нужны функции списка или нужно
убирать элементы добавленные первыми
"""