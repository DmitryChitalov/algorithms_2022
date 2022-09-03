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

Это файл для второго скрипта
"""
"""
Алгоритмы, урок 1, задача 6
используем слоты
до оптимизации 888, после оптимизации 544
сэкономили место
"""

# исходный код
from pympler import asizeof


class TaskBoard:
    def __init__(self):
        self.current_tasks = []
        self.correct_tasks = []
        self.solve_tasks = []
        self.delete_tasks = []

    def __str__(self):
        task_dict = {'current_tasks': self.current_tasks,
                     'correct_tasks': self.correct_tasks,
                     'solve_tasks': self.solve_tasks
                     }
        return str(task_dict)

    def replace_to_current(self, task):
        if task in self.solve_tasks:
            return 'Задача уже решена'
        elif task in self.delete_tasks:
            self.delete_tasks.remove(task)
            self.current_tasks.append(task)
            return 'Задача {} добавлена в текущие'.format(task)
        else:
            self.current_tasks.append(task)
            return 'Задача {} добавлена в текущие'.format(task)

    def replace_to_correct(self, task):
        if task in self.solve_tasks:
            self.solve_tasks.remove(task)
            self.correct_tasks.append(task)
            return 'Решение задачи {} отправлено на корректировку'.format(task)
        else:
            return 'Корректировать можно только решённую задачу'

    def replace_to_solve(self, task):
        if task in self.correct_tasks:
            self.solve_tasks.append(task)
            self.correct_tasks.remove(task)
            return 'Задача {} решена'.format(task)
        elif task in self.current_tasks:
            self.solve_tasks.append(task)
            self.current_tasks.remove(task)
            return 'Задача {} решена'.format(task)
        elif task in self.delete_tasks:
            return 'Задача {} была удалена'.format(task)
        elif task in self.solve_tasks:
            return 'Задача {} уже в списке решённых'.format(task)
        else:
            return 'В решённые можно поместить только задачи из текущего списка или из корректировки'

    def delete(self):
        if len(self.current_tasks) != 0:
            new_current_tasks = self.current_tasks.pop()
            self.delete_tasks.append(new_current_tasks)
            return 'Последняя текущая задача удалена'

        else:
            return 'Нет текущих задач!'

    def basket(self):
        if len(self.delete_tasks) != 0:
            return self.delete_tasks
        else:
            return 'Нет удалённых задач'

    def check(self, task):
        if task in self.current_tasks:
            return 'Задача {} в текущем списке'.format(task)
        elif task in self.solve_tasks:
            return 'Задача была решена'.format(task)
        elif task in self.correct_tasks:
            return 'Задача на корректировке'.format(task)
        elif task in self.delete_tasks:
            return 'Задача была удалена'.format(task)
        else:
            return 'Нет такой задачи'

    def count(self):
        task_dict = {'current_tasks': len(self.current_tasks),
                     'correct_tasks': len(self.correct_tasks),
                     'solve_tasks': len(self.solve_tasks)
                     }
        return task_dict

    def total_delete(self):
        for task in self.current_tasks:
            self.delete_tasks.append(task)
        self.current_tasks.clear()
        return 'Все текущие задачи удалены'


task_board = TaskBoard()
print(task_board) # посмотрим на пустую доску
print(task_board.replace_to_solve('task1')) # попробуем поместить задачу в решённые
print(task_board.replace_to_correct('task1')) # попробуем поместить задачу в корректируемые
print(task_board.replace_to_current('task1')) # накидаем задач в текущий список
print(task_board.replace_to_current('task2'))
print(task_board.replace_to_current('task3'))
print(task_board.replace_to_current('task4'))

print(asizeof.asizeof(task_board))

# оптимизированный код
class TaskBoard_1:
    __slots__ = ['current_tasks', 'correct_tasks', 'solve_tasks', 'delete_tasks']
    def __init__(self):
        self.current_tasks = []
        self.correct_tasks = []
        self.solve_tasks = []
        self.delete_tasks = []

    def __str__(self):
        task_dict = {'current_tasks': self.current_tasks,
                     'correct_tasks': self.correct_tasks,
                     'solve_tasks': self.solve_tasks
                     }
        return str(task_dict)

    def replace_to_current(self, task):
        if task in self.solve_tasks:
            return 'Задача уже решена'
        elif task in self.delete_tasks:
            self.delete_tasks.remove(task)
            self.current_tasks.append(task)
            return 'Задача {} добавлена в текущие'.format(task)
        else:
            self.current_tasks.append(task)
            return 'Задача {} добавлена в текущие'.format(task)

    def replace_to_correct(self, task):
        if task in self.solve_tasks:
            self.solve_tasks.remove(task)
            self.correct_tasks.append(task)
            return 'Решение задачи {} отправлено на корректировку'.format(task)
        else:
            return 'Корректировать можно только решённую задачу'

    def replace_to_solve(self, task):
        if task in self.correct_tasks:
            self.solve_tasks.append(task)
            self.correct_tasks.remove(task)
            return 'Задача {} решена'.format(task)
        elif task in self.current_tasks:
            self.solve_tasks.append(task)
            self.current_tasks.remove(task)
            return 'Задача {} решена'.format(task)
        elif task in self.delete_tasks:
            return 'Задача {} была удалена'.format(task)
        elif task in self.solve_tasks:
            return 'Задача {} уже в списке решённых'.format(task)
        else:
            return 'В решённые можно поместить только задачи из текущего списка или из корректировки'

    def delete(self):
        if len(self.current_tasks) != 0:
            new_current_tasks = self.current_tasks.pop()
            self.delete_tasks.append(new_current_tasks)
            return 'Последняя текущая задача удалена'

        else:
            return 'Нет текущих задач!'

    def basket(self):
        if len(self.delete_tasks) != 0:
            return self.delete_tasks
        else:
            return 'Нет удалённых задач'

    def check(self, task):
        if task in self.current_tasks:
            return 'Задача {} в текущем списке'.format(task)
        elif task in self.solve_tasks:
            return 'Задача была решена'.format(task)
        elif task in self.correct_tasks:
            return 'Задача на корректировке'.format(task)
        elif task in self.delete_tasks:
            return 'Задача была удалена'.format(task)
        else:
            return 'Нет такой задачи'

    def count(self):
        task_dict = {'current_tasks': len(self.current_tasks),
                     'correct_tasks': len(self.correct_tasks),
                     'solve_tasks': len(self.solve_tasks)
                     }
        return task_dict

    def total_delete(self):
        for task in self.current_tasks:
            self.delete_tasks.append(task)
        self.current_tasks.clear()
        return 'Все текущие задачи удалены'


task_board_1 = TaskBoard_1()
print(task_board_1) # посмотрим на пустую доску
print(task_board_1.replace_to_solve('task1')) # попробуем поместить задачу в решённые
print(task_board_1.replace_to_correct('task1')) # попробуем поместить задачу в корректируемые
print(task_board_1.replace_to_current('task1')) # накидаем задач в текущий список
print(task_board_1.replace_to_current('task2'))
print(task_board_1.replace_to_current('task3'))
print(task_board_1.replace_to_current('task4'))

print(asizeof.asizeof(task_board_1))
