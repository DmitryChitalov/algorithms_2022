from memory_profiler import profile
import numpy as np
from random import randint

@profile
def array_list():
    cost = [randint(-100,100)for _ in range(50000)]
    for i in cost:
        a=float(i)
        c=a%1
    res=(f' {int(a//1)} руб {int(float(("%.2f"%c))*100)}коп. ')
    print(res)



@profile
def array_np():
    cost = np.array([randint(-100,100)for _ in range(50000)])
    for i in cost:
        a=float(i)
        c=a%1
    res=(f' {int(a//1)} руб {int(float(("%.2f"%c))*100)}коп. ')
    print(res)





if __name__ == '__main__':
    array_list()
    array_np()


#задание взято из курса основ (2урок 5 задание)
#как видно numpy сильно сжимает массив с данными и использует меньше памяти.
    