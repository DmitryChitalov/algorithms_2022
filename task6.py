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


class TaskClass:

    def __init__(self):
        self.base_task = []
        self.revision_task = []
        self.completed_task = []

    def size_base_task(self):
        if len(self.base_task) == 0:
            print('Задач для проверки не обнаружено:')
            return self.base_task
        else:
            print(f'Для проверки имеется {len(self.base_task)} задач(и):')
            return self.base_task

    def size_revision_task(self):
        if len(self.revision_task) == 0:
            print('Задач на доработку не обнаружено:')
            return self.revision_task
        else:
            print(f'Для доработки имеется {len(self.revision_task)} задач(и):')
            return self.revision_task

    def size_completed_task(self):
        if len(self.completed_task) == 0:
            print('Решенных задач не обнаружено:')
            return self.completed_task
        else:
            print(f'Имеется {len(self.completed_task)} решенных задач(и):')
            return self.completed_task

    def to_base_task(self, item):
        self.base_task.insert(0, item)

    def from_base_task_to_revision_task(self):  # удаляю посл. элем. из base_task и добавляю его в начало revision_task
        self.revision_task.insert(0, self.base_task.pop())
        return self.revision_task[0]

    def from_base_task_to_completed_task(self):  # удаляю посл. элем. из base_task и добав. его в начало completed_task
        self.completed_task.insert(0, self.base_task.pop())
        return self.completed_task[0]

    def from_revision_task_to_completed_task(self):  # удаляю посл. элем. из revision и добав. его в начало completed
        self.completed_task.insert(0, self.revision_task.pop())
        return self.completed_task[0]


if __name__ == '__main__':

    qc_obj = TaskClass()
    print(qc_obj.size_base_task())  # -> Задач для проверки не обнаружено:

    # помещаем объекты в очередь
    qc_obj.to_base_task('my_obj')
    qc_obj.to_base_task(4)
    qc_obj.to_base_task(True)
    qc_obj.to_base_task('rge')
    qc_obj.to_base_task(28)
    qc_obj.to_base_task(False)

    print(qc_obj.size_base_task())  # -> Для проверки имеется 6 задач(и) /n  [False, 28, 'rge', True, 4, 'my_obj']

    print(qc_obj.from_base_task_to_revision_task())  # -> my_obj - задача на доработку
    print(qc_obj.from_base_task_to_completed_task())  # -> 4 - задача решена
    print(qc_obj.from_base_task_to_revision_task())  # -> True - задача на доработку
    print(qc_obj.from_base_task_to_completed_task())  # -> rge - задача решена

    print(qc_obj.size_base_task())  # -> Для проверки имеется 2 задач(и) /n [False, 28]
    print(qc_obj.size_revision_task())  # -> Для доработки имеется 2 задач(и): /n [True, 'my_obj']
    print(qc_obj.size_completed_task())  # -> Имеется 2 решенных задач(и): /n ['rge', 4]

    print(qc_obj.from_revision_task_to_completed_task())  # -> my_obj

    print(qc_obj.size_base_task())  # -> Для проверки имеется 2 задач(и) /n [False, 28]
    print(qc_obj.size_revision_task())  # -> Для доработки имеется 1 задач(и): /n [True]
    print(qc_obj.size_completed_task())  # -> Имеется 3 решенных задач(и): /n ['my_obj', 'rge', 4]



