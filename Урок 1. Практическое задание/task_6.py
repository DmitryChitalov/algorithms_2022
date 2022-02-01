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


class QueueClass:
    def __init__(self):
        self.elems = []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def size(self):
        return len(self.elems)

    def from_queue(self):
        return self.elems.pop()

    def remove(self, other, item):
        other.elems.insert(0, item.from_queue())


if __name__ == '__main__':
    main_tasks = QueueClass()
    imp_tasks = QueueClass()
    # Вставляем задачи
    main_tasks.to_queue('Первая задача')
    main_tasks.to_queue('Вторая задача')
    main_tasks.to_queue('Третья задача')

    print(main_tasks.size())  # Проверяем размер основного списка
    main_tasks.remove(imp_tasks, main_tasks)  # Переносим задачу из основного списка в список доработок
    print(main_tasks.size())  # Проверяем размер основного списка
    print(imp_tasks.size())  # Проверяем размер списка на доработки
    print(imp_tasks.from_queue())  # Смотрим какая задача в списке на доработки
    main_tasks.remove(imp_tasks, main_tasks)
    print(main_tasks.size())  # Проверяем размер основного списка
    print(imp_tasks.size())  # Проверяем размер списка на доработки
    print(imp_tasks.from_queue())  # Смотрим какая задача в списке на доработки
    main_tasks.remove(imp_tasks, main_tasks)
    print(main_tasks.size())  # Проверяем размер основного списка
    print(imp_tasks.size())  # Проверяем размер списка на доработки
    print(imp_tasks.from_queue())  # Смотрим какая задача в списке на доработки
    # Если мы попытаемся перенести еще задачу, выдаст ошибку так как задач в основном списке больше нет
    main_tasks.remove(imp_tasks, main_tasks)

