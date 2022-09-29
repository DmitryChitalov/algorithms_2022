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
class taskboard:

    def __init__(self, tasks_list):
        self.t_for_solution = tasks_list
        self.t_for_correction = []
        self.t_finished = []

    def __str__(self):
        return f'To solve: {str(self.t_for_solution)}, \n' \
               f'to correct: {str(self.t_for_correction)}, \n' \
               f'finished: {str(self.t_finished)}.'

    def to_solve(self):
        if len(self.t_for_solution) == 0:
            print('Все задачи завершены!')
        else:
            self.t_finished.insert(0, self.t_for_solution.pop())

    def to_correct(self):
        if len(self.t_for_solution) == 0:
            print('Задач на исправление нет')
        else:
            self.t_for_correction.insert(0, self.t_for_solution.pop())

    def to_check_corrected(self):
        if len(self.t_for_correction) == 0:
            print('Нет исправленных задач для проверки')
        else:
            self.t_finished.insert(0, self.t_for_correction.pop())


target_tasks = taskboard(['one', 'two', 'three', 'four', 'five'])
target_tasks.to_solve()
target_tasks.to_correct()
target_tasks.to_correct()
target_tasks.to_solve()
target_tasks.to_check_corrected()
target_tasks.to_solve()
target_tasks.to_solve()
print(target_tasks)
target_tasks.to_solve()
