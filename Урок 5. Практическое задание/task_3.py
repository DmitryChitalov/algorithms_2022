"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
import timeit
import random
for_choice = 'qwertyuiopasdfghjklzxcvbnm1234567890'


def create_test_data():
    """Функция создает случайный список и и его точкую копию deque"""
    l_test = [random.choice(for_choice) for _ in range(100000)]
    d_test = deque(l_test)
    return l_test, d_test


list_test, deque_test = create_test_data()
a = timeit.timeit("deque_test.append('0')", globals=globals(), number=100)
b = timeit.timeit("list_test.append('0')", globals=globals(), number=100)
print(f"""Результат выполнения append для deque: {a} """)
print(f"""Результат выполнения append для list: {b} """)
if a < b:
    print(f"""Append deque выполнился быстрее append list на: {(b-a)/a*100}%""")
else:
    print(f"""Append list выполнился быстрее append deque на: {(a-b)/b*100}%""")
"""
Ответ: list.append выполнился быстрее deque.append на: 29%
"""

print()

list_test, deque_test = create_test_data()
a = timeit.timeit("deque_test.pop()", globals=globals(), number=100000)
b = timeit.timeit("list_test.pop()", globals=globals(), number=100000)
print(f"""Результат выполнения pop для deque: {a} """)
print(f"""Результат выполнения pop для list: {b} """)
if a < b:
    print(f"""Pop deque выполнился быстрее pop list на: {(b-a)/a*100}%""")
else:
    print(f"""Pop list выполнился быстрее pop deque на: {(a-b)/b*100}%""")
"""
Ответ: list.pop() и duque.pop() выполняются примерно одинаковое время
"""
print()

list_test, deque_test = create_test_data()
a = timeit.timeit("deque_test.extend('y')", globals=globals(), number=100000)
b = timeit.timeit("list_test.extend('y')", globals=globals(), number=100000)
print(f"""Результат выполнения extend для deque: {a} """)
print(f"""Результат выполнения extend для list: {b} """)
if a < b:
    print(f"""Extend deque выполнился быстрее extend list на: {(b-a)/a*100}%""")
else:
    print(f"""Extend list выполнился быстрее extend deque на: {(a-b)/b*100}%""")
"""
Ответ: deque.extend выполняется намного быстрее. В 39 раз.
"""
print()


list_test, deque_test = create_test_data()
a = timeit.timeit("deque_test.appendleft('y')", globals=globals(), number=1000)
b = timeit.timeit("list_test.insert(0,'y')", globals=globals(), number=1000)
print(f"""Результат выполнения appendleft для deque: {a} """)
print(f"""Результат выполнения insert(0) для list: {b} """)
if a < b:
    print(f"""Appendleft deque выполнился быстрее insert(0) list на: {(b-a)/a*100}%""")
else:
    print(f"""insert(0) list выполнился быстрее appendleft deque на: {(a-b)/b*100}%""")
"""
Ответ: # appendleft выполняется в тысячи раз быстрее, чем insert(0), ['y']+list_test еще дольше
"""
print()

list_test, deque_test = create_test_data()
a = timeit.timeit("deque_test.popleft()", globals=globals(), number=1000)
b = timeit.timeit("list_test.pop(0)", globals=globals(), number=1000)
print(f"""Результат выполнения popleft для deque: {a} """)
print(f"""Результат выполнения pop(0) для list: {b} """)
if a < b:
    print(f"""Popleft deque выполнился быстрее pop(0) list на: {(b-a)/a*100}%""")
else:
    print(f"""pop(0) list выполнился быстрее popleft deque на: {(a-b)/b*100}%""")
"""
Ответ: # popleft выполняется в десятки тысяч раз быстрее 
"""
print()


list_test, deque_test = create_test_data()

a = timeit.timeit("deque_test.extendleft([0,1,10])", globals=globals(), number=1000)
b = timeit.timeit("[0,1,10]+list_test", globals=globals(), number=1000)
print(f"""Результат выполнения extendleft для deque: {a} """)
print(f"""Результат выполнения [0,1,10] для list: {b} """)
if a < b:
    print(f"""Extendleft deque выполнился быстрее [0,1,10] list на: {(b-a)/a*100}%""")
else:
    print(f"""[0,1,10]+list выполнился быстрее extendleft deque на: {(a-b)/b*100}%""")
"""
Ответ: # extendleft выполняется в десятки тысяч раз быстрее
"""
print()

"""Задание 3"""

list_test, deque_test = create_test_data()

a = timeit.timeit("deque_test[456]", globals=globals(), number=1000)
b = timeit.timeit("list_test[456]", globals=globals(), number=1000)
print(f"""Результат получения элемента из deque: {a} """)
print(f"""Результат получения элемента из list: {b} """)
if a < b:
    print(f"""Получения элемента из deque быстрее получения элемента из list на: {(b-a)/a*100}%""")
else:
    print(f"""Получения элемента из list быстрее получения элемента из deque на: {(a-b)/b*100}%""")
"""
Ответ: Получение элемента из list немного быстрее чем из deque
"""
print()
