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
class DequeClass():
    def __init__(self):
        self.tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.tasks_corrects = []
        self.solution_tasks = []

    def solved(self):
        self.solution_tasks.append(self.tasks.pop()) # задачи решены из основного списка

    def correct(self):
        self.tasks_corrects.append(self.tasks.pop()) #задачи для корректировки в список для доработки

    def solution_correct(self):
        self.solution_tasks.append(self.tasks_corrects.pop()) #решенные задачи из списка на доработку

    def __str__(self):
        return f'{self.tasks} - Осталось решить\n{self.tasks_corrects} - на корректировку \n{self.solution_tasks} - решены'


tasks = DequeClass()
tasks.correct()
tasks.correct()
tasks.correct()
tasks.correct()
tasks.correct()
tasks.solved()
tasks.solved()
tasks.solved()
tasks.solution_correct()
tasks.solution_correct()
print(tasks)

