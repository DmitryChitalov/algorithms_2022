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
        self.base_tasks = []
        self.modification_tasks = []
        self.well_done_tasks = []

    def to_base_tasks(self, item):
        self.base_tasks.insert(0, item)

    def from_base_to_modification(self):
        self.modification_tasks.insert(0, self.base_tasks.pop())

    def from_modification_to_well_done(self):
        self.well_done_tasks.insert(0, self.modification_tasks.pop())

    def from_base_to_well_done(self):
        self.well_done_tasks.insert(0, self.base_tasks.pop())


if __name__ == '__main__':
    qc_obj = QueueClass()

    # добавление заданий в основную очередь
    qc_obj.to_base_tasks('task_1')
    qc_obj.to_base_tasks('task_2')
    qc_obj.to_base_tasks('task_3')
    qc_obj.to_base_tasks('task_4')

    # задания в очереди
    print(qc_obj.base_tasks)                # -> ['task_4', 'task_3', 'task_2', 'task_1']

    # перемещение крайней задачи из основной очереди на изменение
    qc_obj.from_base_to_modification()
    print(qc_obj.base_tasks)                # -> ['task_4', 'task_3', 'task_2']
    print(qc_obj.modification_tasks)        # -> ['task_1']

    # перемещение крайней задачи основной очереди в выполненые
    qc_obj.from_base_to_well_done()
    print(qc_obj.base_tasks)                # -> ['task_4', 'task_3']
    print(qc_obj.well_done_tasks)           # -> ['task_2']

    # перемещение задачи из очереди на изменение в выполненые
    qc_obj.from_modification_to_well_done()
    print(qc_obj.base_tasks)                # -> ['task_4', 'task_3']
    print(qc_obj.modification_tasks)        # -> []
    print(qc_obj.well_done_tasks)           # -> ['task_1', 'task_2']