import random


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


def distribution(name_str: dict, exercises: list):
    for exercise in exercises:
        name_str['Basic'].to_queue(exercise)  # заполнили очередь задачками

    while name_str['Basic'].is_empty() == 0:
        ex = name_str['Basic'].from_queue()
        solution = solve(ex)
        if solution == 1:
            name_str['Solved'].to_queue(ex)
        else:
            name_str['Unsolved'].to_queue(ex)


def solve(exercise):
    """
    здесь задачки должны перераспр на решения, возвращаемый параметр - булевский
    true если решилась, false - если на доработку
    """
    return bool(random.randint(0, 1))


basic_queue = QueueClass()
solved_queue = QueueClass()
unsolved_queue = QueueClass()
structure = {'Basic': basic_queue, 'Solved': solved_queue, 'Unsolved': unsolved_queue}
distribution(structure, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # номер задачи
print('Очередь базовая:', basic_queue.elems)  # как и должно быть - пусто
print('Очередь решеных:', solved_queue.elems)  # решеные
print('Очередь на доработку:', unsolved_queue.elems)  # на доработку
distribution(structure, [11, 12, 13, 14, 15])
print('Очередь базовая:', basic_queue.elems)
print('Очередь решеных:', solved_queue.elems)
print('Очередь на доработку:', unsolved_queue.elems)
