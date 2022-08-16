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

    def push_in(self, task):
        """Функция добавляет задачу на доску"""
        self.task_desk.append(task)

    def get_now_task(self):
        """Функция проверяет текущую задачу"""
        return self.task_desk[0]

    def task_desk_size(self):
        """Функция показывает сколько задач осталось на доске"""
        return len(self.task_desk)


class TaskDeskBase(TaskDesk):
    """Дочерний класс Базовая доска задач"""
    def __init__(self):
        self.base_desk = TaskDesk.__init__(self)
        self.task = self.task_desk

    def change_status(self, obj):
        """Функция переносящая задачу из Базовой доски в другую доску"""
        self.task_desk.pop(0)
        obj.push_in(self.task)


class TaskDeskDone(TaskDesk):
    """Дочерний класс Доска выполненых задач"""
    def __init__(self):
        self.done_desk = TaskDesk.__init__(self)


class TaskDeskBack(TaskDesk):
    """Дочерний класс Доска задач на доработку"""
    def __init__(self):
        self.back_desk = TaskDesk.__init__(self)
        self.task = self.task_desk

    def change_status(self, obj):
        """Функция переносящая задачу из Базовой доски в другую доску"""
        self.task_desk.pop(0)
        obj.push_in(self.task)


if __name__ == '__main__':
    desk = TaskDesk

"""Функции для сценариев проверки работы структуры"""

desk_dict = {
    'TaskDeskBase': 'Базовая доска задач',
    'TaskDeskDone': 'Доска выполненых задач',
    'TaskDeskBack': 'Доска задач на доработку'
}


def show_next_task(desk_in: TaskDesk):
    """Функция принимает в себя наименование объекта и выводит сообщение о следующей задаче"""
    try:
        print(
            f'Первая задача в {desk_dict[desk_in.__class__.__name__]} : {desk_in.get_now_task()}')
    except IndexError:
        print(f'Задач в {desk_dict[desk_in.__class__.__name__]} нет')


def show_num_task(desk_in: TaskDesk):
    """Функция принимает в себя наименование объекта и выводит сообщение об оставшихся задачах"""
    print(f'Всего задач в {desk_dict[desk_in.__class__.__name__]} : {desk_in.task_desk_size()}')


def push_in(task: str):
    """Функция принимает в себя текст задачи, добавляет задачу в список и сообщает об этом пользователю.
    Предполагается что создавать задачи можно только в Базовой доске задач"""
    desk_base.push_in(task)
    print(f'В доску {desk_dict[desk_base.__class__.__name__]} добавлена задача {task}')


def changestatus(desk_from: TaskDesk, desk_to: TaskDesk):
    """Функция принимает в себя наименование объектов.
    Переносит задачу из одного объекта в другой и выводит сообщение об этом"""
    task = desk_from.get_now_task()
    desk_from.change_status(desk_to)
    print(f'Задача "{task}" перенеена из {desk_dict[desk_from.__class__.__name__]} в '
          f'{desk_dict[desk_to.__class__.__name__]}')


"""Сценарий исполнения"""


desk_base = TaskDeskBase()  # Создаем объект "Базовая доска задач"
print('Создаем новый объект "Базовая доска задач"')
push_in('Monday: buy pencil')
push_in('Tusday: repair door')
push_in('Friday: Beer day!')
print()
show_next_task(desk_base)
show_num_task(desk_base)
print()
desk_done = TaskDeskDone()  # Создаем новый объект "Доска выполненых задач"
print('Создаем новый объект "Доска выполненых задач"')
show_next_task(desk_done)
show_num_task(desk_done)
print()
changestatus(desk_base, desk_done)
show_next_task(desk_base)
show_num_task(desk_base)
show_next_task(desk_done)
show_num_task(desk_done)
print()
desk_back = TaskDeskBack()
print('Создаем новый объект "Доска задач на доработку"')
changestatus(desk_base, desk_back)
show_next_task(desk_back)
show_num_task(desk_back)
show_next_task(desk_base)
show_num_task(desk_done)
