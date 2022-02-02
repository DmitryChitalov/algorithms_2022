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


class ToDoClass:
    def __init__(self):
        self.elements = []

    def add_task(self, item):
        self.elements.insert(0, item)

    def size(self):
        return len(self.elements)

    def from_queue(self):
        return self.elements.pop()

    def relocate(self, other, item):
        other.elements.insert(0, item.from_queue())


if __name__ == '__main__':
    main_tasks = ToDoClass()
    imp_tasks = ToDoClass()

    main_tasks.add_task('Убрать квартиру')
    main_tasks.add_task('Приготовить ужин на вечер')
    main_tasks.add_task('Купить пылесос')
    main_tasks.add_task('Тренировка')

    print(main_tasks.size())  # Смотрим размер основного списка задач
    main_tasks.relocate(imp_tasks, main_tasks)  # Переносим задачу из основного списка в список доработок
    print(imp_tasks.size())  # Смотрим размер списка на доработки
    print(imp_tasks.from_queue())  # Смотрим какая задача в списке на доработки
