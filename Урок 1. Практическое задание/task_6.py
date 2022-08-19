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
        self.base_tasks = []
        self.reworking = []
        self.resolved = []

    def add_task(self, *name):
        """добавляет задачи"""
        for i in name:
            self.base_tasks.insert(0, i)

    def from_base_to_resolved(self):
        """отправляет базовые задачи в решенные"""
        self.resolved.insert(0, self.base_tasks.pop())

    def from_base_to_rework(self):
        """отправка на доработку"""
        self.reworking.insert(0, self.base_tasks.pop())

    def from_rework_to_resolved(self):
        """отправка в решенные из доработки"""
        self.resolved.insert(0, self.reworking.pop())

    def show_tasks(self):
        """показывает все очереди"""
        print('Базовые задачи:', self.base_tasks)
        print('Задачи в доработке:', self.reworking)
        print('Решенные задачи:', self.resolved)

    def show_base(self):
        print('Базовые задачи:', self.base_tasks)

    def show_reworking(self):
        print('Задачи в доработке:', self.reworking)

    def show_resolved(self):
        print('Решенные задачи:', self.resolved)


if __name__ == '__main__':
    table = Taskboard()
    table.show_tasks()
    print('*'*100)
    table.add_task('satellite')
    table.add_task('man in space', 'fly to Moon', 'search for extraterrestrial life', 'AI development', 'World Wide Web', 'flight to Mars', 'MoonBase', 'transgalactic flight')
    table.show_tasks()
    print('*'*100)
    table.add_task('immortality')
    table.from_base_to_resolved() #решено
    table.from_base_to_resolved() #решено
    table.show_tasks()
    print('*'*100)
    table.from_base_to_resolved() #решено
    table.from_base_to_rework() #в доработке
    table.from_base_to_rework() #в доработке
    table.show_tasks()
    print('*'*100)
    table.from_base_to_resolved() #в доработке
    table.from_base_to_rework() #в доработке
    table.from_base_to_rework() #в доработке
    table.show_tasks()
    print('*'*100)
    table.from_base_to_rework() #в доработке
    table.from_base_to_rework() #в доработке
    table.from_rework_to_resolved()
    table.from_rework_to_resolved()
    table.add_task('???')
    table.show_tasks()
    print('*'*100)
    table.from_rework_to_resolved()
    table.from_rework_to_resolved()
    table.show_tasks()
    print('*'*100)
    table.from_rework_to_resolved()
    table.show_tasks()
    print('*'*100)
