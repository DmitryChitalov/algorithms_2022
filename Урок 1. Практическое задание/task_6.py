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

class Task:
    def __init__(self):
        # Имеем в начале где то хранящиеся списки задач (наверняка в БД)
        # Базовый список задач
        self.tasks_base = []
        # Список задач на доработку
        self.tasks_revision = []
        # Список завершенных задач
        self.tasks_solved = []
        # Задача, это тоже список данных, таких как:
        # сама задача, ответственный, срок, статус выполнения
        self.task = []

    def new(self, task : str, responsible : str, period : str, status : str):
        self.task.append(task)
        self.task.append(responsible)
        self.task.append(period)
        self.task.append(status)
        self.tasks_base.append(self.task)
        self.task = []

    def base_to_revision(self, num_base : int):
        self.task = self.tasks_base.pop(num_base - 1)
        self.task[3] = 'revision'
        self.tasks_revision.append(self.task)
        self.task = []

    def base_to_solved(self, num_base : int):
        self.task = self.tasks_base.pop(num_base - 1)
        self.task[3] = 'solved'
        self.tasks_solved.append(self.task)
        self.task = []

    def revision_to_solved(self, num_base : int):
        self.task = self.tasks_revision.pop(num_base - 1)
        self.task[3] = 'solved'
        self.tasks_solved.append(self.task)
        self.task = []

    def print(self):
        print('Текущий список задач:\n', self.tasks_base)
        print('Текущий список задач в доработке:\n', self.tasks_revision)
        print('Выполненные задачи:\n', self.tasks_solved)

if __name__ == '__main__':
    tasks = Task()
    tasks.new('Первая задача', 'ИвановИИ', '2022-09-28', 'new')
    tasks.new('Вторая задача', 'ИвановИИ', '2022-09-28', 'new')
    tasks.new('Третья задача', 'ИвановИИ', '2022-09-28', 'new')
    tasks.new('Четвертая задача', 'ИвановИИ', '2022-09-28', 'new')
    tasks.new('Пятая задача', 'ИвановИИ', '2022-09-28', 'new')
    tasks.print()
    tasks.base_to_revision(2)
    tasks.print()
    tasks.base_to_solved(3)
    tasks.print()
    tasks.base_to_revision(3)
    tasks.revision_to_solved(1)
    tasks.print()