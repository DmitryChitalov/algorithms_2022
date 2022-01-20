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
Это файл для первого скрипта
"""


from pympler import asizeof


class TaskBoard:
    def __init__(self):
        self.new_tasks = []
        self.incorrect = []
        self.solved = []

    def size(self):
        task_board = {
            'new_tasks': len(self.new_tasks),
            'solved': len(self.solved),
            'incorrect': len(self.incorrect)
        }
        return task_board

    def add_new_task(self, task):
        self.new_tasks.insert(0, task)

    def get_new_task(self):
        return self.new_tasks.pop()

    def task_solved(self, task):
        self.solved.insert(0, task)

    def check_task(self):
        return self.solved.pop()

    def task_incorrect(self, task):
        self.incorrect.insert(0, task)

    def correct_task(self):
        return self.incorrect.pop()


task_board = TaskBoard()

for i in range(5):
    task_board.add_new_task(f'task_{i}')

current_task_1 = task_board.get_new_task()
task_board.task_solved(current_task_1)
current_task_2 = task_board.get_new_task()
task_board.task_solved(current_task_2)
check_task = task_board.check_task()
task_board.task_incorrect(check_task)
correct_task = task_board.correct_task()
task_board.task_solved(correct_task)

print(asizeof.asizeof(task_board))

########################################################################################


class TaskBoardOpt:
    __slots__ = ['new_tasks', 'incorrect', 'solved']

    def __init__(self):
        self.new_tasks = []
        self.incorrect = []
        self.solved = []

    def size(self):
        task_board = {
            'new_tasks': len(self.new_tasks),
            'solved': len(self.solved),
            'incorrect': len(self.incorrect)
        }
        return task_board

    def add_new_task(self, task):
        self.new_tasks.insert(0, task)

    def get_new_task(self):
        return self.new_tasks.pop()

    def task_solved(self, task):
        self.solved.insert(0, task)

    def check_task(self):
        return self.solved.pop()

    def task_incorrect(self, task):
        self.incorrect.insert(0, task)

    def correct_task(self):
        return self.incorrect.pop()


task_board2 = TaskBoardOpt()

for i in range(5):
    task_board2.add_new_task(f'task_{i}')

current_task_1 = task_board2.get_new_task()
task_board2.task_solved(current_task_1)
current_task_2 = task_board2.get_new_task()
task_board2.task_solved(current_task_2)
check_task = task_board2.check_task()
task_board2.task_incorrect(check_task)
correct_task = task_board2.correct_task()
task_board2.task_solved(correct_task)

print(asizeof.asizeof(task_board2))

# использование слотов экономит память
