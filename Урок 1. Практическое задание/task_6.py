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
class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)  # добавим элементы в очередь

    def from_queue(self):
        return self.elems.pop()  # выведем элементы из очереди

    def size(self):
        return len(self.elems)  # размер очереди

    def remove(self, other, item):
        other.elems.insert(0, item.from_queue())  # перенос элементов в другую очередь


if __name__ == '__main__':
    basic_tasks = QueueClass()  # Основная очередь
    rev_tasks = QueueClass()    # Очередь на доработку
    solv_task = QueueClass()  # Решённые задачи
    print(basic_tasks.is_empty())  # -> True. Основная очередь пустая

    # помещаем объекты в основную очередь
    basic_tasks.to_queue('first')
    basic_tasks.to_queue('second')
    basic_tasks.to_queue('third')
    basic_tasks.to_queue('fourth')
    basic_tasks.to_queue('fifth')

    print(basic_tasks.is_empty())  # -> False. Основная очередь не пустая

    print(rev_tasks.is_empty())  # -> True. Очередь для доработки пустая

    print(solv_task.is_empty())  # -> True. Список решений пуст

    print(basic_tasks.size())  # -> 5

    print()
    # Переносим задачу в список задач на доработку
    basic_tasks.remove(rev_tasks, basic_tasks)

    print(basic_tasks.size())  # -> 4

    print(rev_tasks.size())    # -> 1

    print(solv_task.size())  # -> 0

    print()
    # Переносим задачу в список задач на доработку
    basic_tasks.remove(rev_tasks, basic_tasks)

    # Переносим задачи в список решённых задач
    solv_task.to_queue(basic_tasks.from_queue())
    solv_task.to_queue(rev_tasks.from_queue())

    print()

    print(basic_tasks.size())  # -> 2

    print(solv_task.size()) # -> 2

    print(rev_tasks.size())  # -> 1