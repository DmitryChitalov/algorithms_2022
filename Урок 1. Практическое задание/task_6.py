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

class Tasks:

    def __init__(self, tasks_list):
        self.t_for_solution = tasks_list
        self.t_for_correction = []
        self.t_solved = []

    def __str__(self):
        return f'To solve: {str(self.t_for_solution)}, \n' \
               f'to correct: {str(self.t_for_correction)}, \n' \
               f'solved: {str(self.t_solved)}.'

    def to_solve(self):
        if len(self.t_for_solution) == 0:
            print('There are no tasks to solve.')
        else:
            self.t_solved.insert(0, self.t_for_solution.pop())

    def to_correct(self):
        if len(self.t_for_solution) == 0:
            print('There are no tasks to correct.')
        else:
            self.t_for_correction.insert(0, self.t_for_solution.pop())

    def to_check_corrected(self):
        if len(self.t_for_correction) == 0:
            print('There are no corrected tasks to check.')
        else:
            self.t_solved.insert(0, self.t_for_correction.pop())


current_tasks = Tasks(['task_1', 'task_2', 'task_3', 'task_4', 'task_5'])
current_tasks.to_solve()
current_tasks.to_correct()
current_tasks.to_correct()
current_tasks.to_solve()
current_tasks.to_check_corrected()
current_tasks.to_solve()
print(current_tasks)
current_tasks.to_solve()