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
        self.tasks = []
        self.finalize = []
        self.completed = []

    def add_task(self, task, condition):
        if condition == 'В работу':
            self.tasks.insert(0, task)
        elif condition == 'На доработку':
            self.finalize.insert(0, task)
        elif condition == 'Выполнено':
            self.completed.insert(0, task)

    def view_task(self, lst_tasks):
        if lst_tasks == 'В работу' and self.tasks:
            return self.tasks.pop()
        elif lst_tasks == 'На доработку' and self.finalize:
            return self.finalize.pop()
        elif lst_tasks == 'Выполнено' and self.completed:
            return self.completed.pop()
        else:
            return f'Список задач пуст'

    def view_number_tasks(self, name_lst):
        if name_lst == 'В работу' and self.tasks:
            return f'В работе: {self.tasks}'
        elif name_lst == 'На доработку' and self.finalize:
            return f'На доработке: {self.finalize}'
        elif name_lst == 'Выполнено' and self.completed:
            return f'Выполненные: {self.completed}'
        elif name_lst == 'Все':
            return f'В работу: {self.tasks} Выполненные: {self.completed} На доработку: {self.finalize}'
        else:
            return f'Список задач пуст'


tsk = TaskBoard()

# Заполняем доску задачами
tsk.add_task('Задача1', 'В работу')
tsk.add_task('Задача2', 'В работу')
tsk.add_task('Задача3', 'В работу')
tsk.add_task('Задача4', 'В работу')
tsk.add_task('Задача5', 'В работу')
tsk.add_task('Задача6', 'В работу')
tsk.add_task('Задача7', 'В работу')

# Берём задачу с доски основной, смотрим и решаем куда разместить, на доработку или в выполненные
task_1 = tsk.view_task('В работу')
tsk.add_task(task_1, 'На доработку')

task_2 = tsk.view_task('В работу')
tsk.add_task(task_2, 'Выполнено')

# Смотрим всё наши доски с очередями задач, можно посмотреть по одной из выбранных очередей
print(tsk.view_number_tasks('Все'))

