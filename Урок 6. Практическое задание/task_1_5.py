"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""


from sys import getsizeof


# ИСХОДНОЕ:
class Matrix:

    def __init__(self, some_list):
        self.some_list = some_list

    def __str__(self):
        for el in self.some_list:
            print('|', end=' ')
            for i in el:
                print(f'{i}', end=' ')
            print('|')
        return

    def __add__(self, other):
        res = self.some_list.copy()
        for i in range(len(self.some_list)):
            if len(self.some_list) != len(other.some_list):
                print(f'Списки разной длины. Проверьте.')
                exit(code=1)
            for j in range(len(self.some_list[i])):
                if len(self.some_list[i]) != len(other.some_list[i]):
                    print(f'Списки разной длины. Проверьте.')
                    exit(code=1)
                res[i][j] = self.some_list[i][j] + other.some_list[i][j]
        return res


# ОПТИМИЗИРОВАННОЕ:
class Matrix2:
    __slots__ = 'some_list'

    def __init__(self, some_list):
        self.some_list = some_list

    def __str__(self):
        for el in self.some_list:
            print('|', end=' ')
            for i in el:
                print(f'{i}', end=' ')
            print('|')
        return

    def __add__(self, other):
        res = self.some_list.copy()
        for i in range(len(self.some_list)):
            if len(self.some_list) != len(other.some_list):
                print(f'Списки разной длины. Проверьте.')
                exit(code=1)
            for j in range(len(self.some_list[i])):
                if len(self.some_list[i]) != len(other.some_list[i]):
                    print(f'Списки разной длины. Проверьте.')
                    exit(code=1)
                res[i][j] = self.some_list[i][j] + other.some_list[i][j]
        return res


f_list = [[31, 22], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]
s_list = [[31, 22], [37, 43], [51, 86], [3, 5, 32], [2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]]

# До
first_el = Matrix(f_list)
second_el = Matrix(s_list)
result_list = first_el + second_el
result = Matrix(result_list)
print(getsizeof(result))

# После
first_el = Matrix2(f_list)
second_el = Matrix2(s_list)
result_list = first_el + second_el
result = Matrix2(result_list)
print(getsizeof(result))

"""
48
40
Вывод:
Использование слотов позволяет экономить память при использовании ООП.
"""