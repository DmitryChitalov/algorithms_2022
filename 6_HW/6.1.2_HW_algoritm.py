"""1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
"""
"""__________________________________________________________________________________________________________________
Оптимизировал задание 1 урока 10 курса основ. В слотах класса изменил хранение атрибутов в словаре на список, 
что займет меньше памяти."""
from pympler import asizeof


# решение до усовершенствования 840
class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Problems with shape'
        return answer


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
print(asizeof.asizeof(matrix_1))

# решение после усовершенствования 672
class Matrix:
    __slots__ = ['input_data']

    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Problems with shape'
        return answer


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
print(asizeof.asizeof(matrix_1))




