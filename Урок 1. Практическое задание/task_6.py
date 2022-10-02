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


class Taskboard:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def remove(self, other, item):
        return other.elems.insert(0, item.from_queue())


if __name__ == '__main__':
    basic_tasks = Task_Board_Class()
    rework_tasks = Task_Board_Class()
    print(basic_tasks.is_empty())  # -> True. Основная очередь пустая
    print(rework_tasks.is_empty())  # -> True. Основная очередь пустая

    # помещаем объекты в основную очередь
    basic_tasks.to_queue('task1')
    basic_tasks.to_queue('task2')
    basic_tasks.to_queue('task3')
    basic_tasks.to_queue('task4')

    print(basic_tasks.is_empty())  # -> False. Основная очередь не пустая
    print(basic_tasks.size())  # -> 4
    print(rework_tasks.is_empty())  # -> True. Очередь для доработки пустая

    # Переносим задачу 'task1' в список задач на доработку
    basic_tasks.remove(rework_tasks, basic_tasks)

    print(basic_tasks.size())  # -> 3
    print(rework_tasks.size())  # -> 1

    print(basic_tasks.elems)  # -> ['task4', 'task3', 'task2']
    print(rework_tasks.elems)  # -> ['task1']
