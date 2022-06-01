"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
class TaskBoard:
    def __init__(self):
        self.new_tasks = []
        self.solved = []
        self.for_correction = []

    def size(self):
        s = {
            'new_tasks': len(self.new_tasks),
            'solved': len(self.solved),
            'for_correction': len(self.for_correction)
        }
        return s

    def add_new_task(self, task):
        self.new_tasks.insert(0, task)

    def get_new_task(self):
        return self.new_tasks.pop()

    def task_solved(self, task):
        self.solved.insert(0, task)

    def check_task(self):
        return self.solved.pop()

    def task_for_correction(self, task):
        self.for_correction.insert(0, task)

    def fix_task(self):
        return self.for_correction.pop()

task_board = TaskBoard()
print(task_board.size())

for i in range(10):
    task_board.add_new_task(f'task_{i}')

current_task = task_board.get_new_task()
print(current_task)
task_board.task_solved(current_task)

current_task = task_board.get_new_task()
print(current_task)
task_board.task_for_correction(current_task)

current_task = task_board.get_new_task()
print(current_task)
task_board.task_for_correction(current_task)

print(task_board.size())

check_task = task_board.check_task()
print(check_task)
task_board.task_for_correction(check_task)

print(task_board.size())

fix_task = task_board.fix_task()
print(fix_task)
task_board.task_solved(fix_task)

fix_task = task_board.fix_task()
print(fix_task)
task_board.task_solved(fix_task)

print(task_board.size())