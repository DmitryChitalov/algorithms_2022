"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
class ListClass:
    def __init__(self):
        self.queue = []

    def to_list(self, task):
        self.queue.append(task)

    def from_list(self, task):
        self.queue.remove(task)

    def empty_list(self):
        return self.queue == []

class TaskBoard:
    def __init__(self):
        self.base_queue = ListClass()
        self.solved_queue = ListClass()
        self.modify_queue = ListClass()

    def __str__(self):
        if self.base_queue:
            return f'Ваш базовый список задач: {str(self.base_queue.queue)}'
        else:
            return 'Ваш  базовый список задач пуст.'

    def add_to_base(self, task):
        self.base_queue.to_list(task)

    def solved_task(self, task):
        self.base_queue.from_list(task)
        self.solved_queue.to_list(task)
        return f'Ваш список решенных задач: {self.solved_queue.queue}'

    def modified_task(self, task):
        self.base_queue.from_list(task)
        self.modify_queue.to_list(task)
        return f'Ваш список задач, отправленных на доработку: {self.modify_queue.queue}'

    def from_modify_to_base(self, task):
        self.modify_queue.from_list(task)
        self.base_queue.to_list(task)
        print(f'Задача {task} доработана и перемещена в базовый список')


if __name__ == '__main__':
    user1 = TaskBoard()
    user1.add_to_base('task1')
    user1.add_to_base('task2')
    user1.add_to_base('task3')
    user1.add_to_base('task4')
    print(user1)
    print(user1.solved_task('task1'))
    print(user1)
    print(user1.modified_task('task4'))
    print(user1)
    user1.from_modify_to_base('task4')
    print(user1)
