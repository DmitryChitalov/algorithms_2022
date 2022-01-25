"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

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
print(task_board.size())

for i in range(5):
    task_board.add_new_task(f'task_{i}')

current_task_1 = task_board.get_new_task()
print(current_task_1)
task_board.task_solved(current_task_1)

current_task_2 = task_board.get_new_task()
print(current_task_2)
task_board.task_solved(current_task_2)

print(task_board.size())

check_task = task_board.check_task()
print(check_task)
task_board.task_incorrect(check_task)

print(task_board.size())

correct_task = task_board.correct_task()
print(correct_task)
task_board.task_solved(correct_task)

print(task_board.size())