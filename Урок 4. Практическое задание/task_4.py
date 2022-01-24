"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""

# ==============================================================================
# === Ответ ====================================================================
# ==============================================================================
# func_1 --- input_len_array = 3 --- min_time =     7.998896762728691e-07  <=== лучший результат, при малой длине массива
# func_2 --- input_len_array = 3 --- min_time =     1.00000761449337e-06
# func_3 --- input_len_array = 3 --- min_time =     9.00006853044033e-07   <=== второе место, при малой длине массива
# func_4 --- input_len_array = 3 --- min_time =     4.499917849898338e-06
# ======================================================================
# func_1 --- input_len_array = 30 --- min_time =    1.0599964298307896e-05
# func_2 --- input_len_array = 30 --- min_time =    1.2599979527294636e-05
# func_3 --- input_len_array = 30 --- min_time =    1.0100076906383038e-05 <=== второе место, при небольшой длине массива
# func_4 --- input_len_array = 30 --- min_time =    5.499925464391708e-06  <=== лучший результат, при небольшой длине массива
# ======================================================================
# func_1 --- input_len_array = 300 --- min_time =   0.0008549999911338091
# func_2 --- input_len_array = 300 --- min_time =   0.0008780000498518348
# func_3 --- input_len_array = 300 --- min_time =   0.0008437000215053558  <=== второе место, при небольшой длине массива
# func_4 --- input_len_array = 300 --- min_time =   3.120000474154949e-05  <=== лучший результат, при приличной длине массива
# ======================================================================
# func_1 --- input_len_array = 3000 --- min_time =  0.08700609998777509
# func_2 --- input_len_array = 3000 --- min_time =  0.08586510003078729
# func_3 --- input_len_array = 3000 --- min_time =  0.0854152999818325     <=== второе место, при небольшой длине массива
# func_4 --- input_len_array = 3000 --- min_time =  0.00020570005290210247 <=== лучший результат, при большой длине массива
# ======================================================================
# В варианте func_3 с функцией Counter(array).most_common(1) 
# получился лучший результат с точки зрения времени, так как данная функция 
# хорошо оптимизированна.



from timeit import repeat, default_timer
import random
from collections import Counter


funcs = []

def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

funcs.append("func_1")

# ====================================
def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

funcs.append("func_2")

# ====================================
def func_3(array):
    elem = max(array, key=array.count)
    return (f'Чаще всего встречается число {elem}, '
           f'оно появилось в массиве {array.count(elem)} раз(а)')

funcs.append("func_3")

# ====================================
def func_4(array):
    elem, count = Counter(array).most_common(1)[0]
    return (f'Чаще всего встречается число {elem}, '
           f'оно появилось в массиве {count} раз(а)')

funcs.append("func_4")

for degree in range(4):
    input_len_array = 3*10**degree
    array = random.choices(range(input_len_array//2), k=input_len_array)
    for func in funcs:
        print(f'{f"{func} --- {input_len_array = } --- min_time = ":50}'+
          str(min(repeat(f'{func}(array)', default_timer, globals=globals(), repeat=3, number=1))))
    print('='*70)





