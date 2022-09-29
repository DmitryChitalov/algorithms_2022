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
        self.base = []  # Базовая очередь
        self.revision = []  # Очередь на доработку
        self.completed = []  # Решенные задачи

    def base_is_empty(self):  # Пуста ли базовая очередь?
        return self.base == []

    def revision_is_empty(self):  # Есть ли задачи в очереди на доработку?
        return self.revision == []

    def completed_is_empty(self):  # Завершил ли ты хоть одну задачу?
        return self.completed == []

    def send_task_to_base(self, task):  # получаем задачу
        self.base.insert(0, task)

    def completed_from_base(self):  # Завершаем задачу
        task = self.base.pop()
        self.completed.insert(0, task)

    def send_task_from_base_to_revision(self):  # Задача отправляется на доработку
        task = self.base.pop()
        self.revision.insert(0, task)

    def completed_from_revision(self):  # Задача завершается после доработки
        task = self.revision.pop()
        self.completed.insert(0, task)


if __name__ == '__main__':
    my_desk = TaskBoard()

    # Проверяем пустая ли доска задач
    print(my_desk.base_is_empty())
    print(my_desk.revision_is_empty())
    print(my_desk.completed_is_empty())

    # Получаю задачи от руководителя
    my_desk.send_task_to_base('задача 1')
    my_desk.send_task_to_base('задача 2')
    my_desk.send_task_to_base('задача 3')

    # Проверяю появились ли задачи
    print(my_desk.base_is_empty())

    # Выполняю первую задачу
    my_desk.completed_from_base()

    # Отправляю задачу на доработку
    my_desk.send_task_from_base_to_revision()

    # Выполняю последнюю задачу в моем списке дел
    my_desk.completed_from_base()

    # Задача после исправления решена
    my_desk.completed_from_revision()

    # Есть ли сегодня еще задачи?
    if my_desk.base_is_empty():
        print('Ура, Добби свободен!))')
