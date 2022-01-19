"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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

Это файл для третьего скрипта
"""
from memory_profiler import profile
class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    @property
    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'some problems'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'some problems'
        return answer
@profile
def create_matrix():
    matrix_1 = []
    for i in range(2000):
        matrix_1.append(Matrix([[i for i in range(10)], [i for i in range(10)], [i for i in range(10)]]))
    matrix_2 = []
    for i in range(2000):
        matrix_2.append(Matrix([[i for i in range(10)], [i for i in range(10)], [i for i in range(10)]]))
    return (matrix_1 + matrix_2)
create_matrix()

class Matrix_2:
    __slots__ = ['input_data']
    def __init__(self, list_data):
        self.input_data = list_data

    @property
    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input_data])

    def __add__(self, other):
        answer = ''
        if len(self.input_data) == len(other.input_data):
            for line_1, line_2 in zip(self.input_data, other.input_data):
                if len(line_1) != len(line_2):
                    return 'some problems'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'some problems'
        return answer
@profile
def create_matrix_2():
    matrix_1 = []
    for i in range(2000):
        matrix_1.append(Matrix_2([[i for i in range(10)], [i for i in range(10)], [i for i in range(10)]]))
    matrix_2 = []
    for i in range(2000):
        matrix_2.append(Matrix_2([[i for i in range(10)], [i for i in range(10)], [i for i in range(10)]]))
    return (matrix_1 + matrix_2)
create_matrix_2()

"""
В превом случаю фунция создания и слияния матриц: 3.2 MIB 
во втором случае,где использовал слоты: 1.6 MIB
"""