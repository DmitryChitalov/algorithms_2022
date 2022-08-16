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


class TaskDesk:
    """Общий родительский класс для всех досок задач"""
    def __init__(self):
        self.task_desk = []

    def is_empty(self):
        """Функция проверяет является ли """
        return self.task_desk == []

    def push_in(self, task):
        self.task_desk.append(task)

    def get_now_task(self):
        return self.task_desk[0]

    def task_desk_size(self):
        return len(self.task_desk)


class TaskDeskBase(TaskDesk):
    def __init__(self):
        self.base_desk = TaskDesk.__init__(self)

    def change_status(self, obj):
        self.task = self.task_desk.pop(0)
        obj.push_in(self.task)



class TaskDeskDone(TaskDesk):
    def __init__(self):
        self.done_desk = TaskDesk.__init__(self)


class TaskDeskBack(TaskDesk):
    def __init__(self):
        self.back_desk = TaskDesk.__init__(self)

    def change_status(self, obj):
        self.task = self.task_desk.pop(0)
        obj.push_in(self.task)


if __name__ == '__main__':
    desk = TaskDesk


desk_base = TaskDeskBase()  # Создаем объект базовой очереди задач
desk_base.push_in('Monday: buy pencil')  # В базовую очередь задач добавляем первую задачу
desk_base.push_in('Tusday: repair door')  # В базовую очередь задач добавляем вторую задачу
desk_base.push_in('Wednesday: You turn to walk with dog')  # В базовую очередь задач добавляем третью задачу
desk_base.push_in('Friday: Beer day!')  # В базовую очередь задач добавляем четвертую задачу
print(desk_base.get_now_task())  # Какая задача сейчас первая в базовой очереди задач???
print(desk_base.task_desk_size())  # Сколько всего задач в базовой очереди задач
desk_done = TaskDeskDone()  # Создаем объект очереди выполненых задач
print(desk_done.task_desk_size())
try:
    print(desk_done.get_now_task())  # Какая задача сейчас первая в базовой очереди задач???
except IndexError:
    print('Задач в очереди нет')
desk_base.change_status(desk_done)  # Выполним задачу
try:
    print(desk_done.get_now_task())  # Какая задача сейчас первая в базовой очереди задач???
except IndexError:
    print('Задач в очереди нет')
print(desk_base.get_now_task())  # Какая задача сейчас первая в базовой очереди задач???
desk_base.change_status(desk_done)  # Выполним задачу
print(desk_base.get_now_task())  # Какая задача сейчас первая в базовой очереди задач???
print(desk_done.task_desk_size())
desk_back = TaskDeskBack()
desk_base.change_status(desk_back)  # Перенесем задачу в доработку
print(desk_base.get_now_task())  # Какая задача сейчас первая в базовой очереди задач???
print(desk_back.get_now_task())  # Какая задача сейчас первая в базовой очереди задач???
print(desk_back.task_desk_size())
