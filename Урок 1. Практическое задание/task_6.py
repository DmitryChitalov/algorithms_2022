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
        self.new_tasks = []
        self.done_tasks = []
        self.to_fix_tasks = []

    def is_empty(self, checked_queue):
        if checked_queue == 'new_tasks':
            return self.new_tasks == []
        elif checked_queue == 'tasks_to_fix':
            return self.to_fix_tasks == []
        else:
            return self.done_tasks == []

    def todo_queue(self, item):
        self.new_tasks.insert(0, item)

    def move_between_queue(self, from_queue):
        if from_queue == 'new_tasks':
            self.done_tasks.insert(0, self.new_tasks.pop())
        elif from_queue == 'from_fix_tasks':
            self.done_tasks.insert(0, self.to_fix_tasks.pop())
        else:
            self.to_fix_tasks.insert(0, self.new_tasks.pop())

    def size(self, queue):
        if queue == 'new_tasks':
            return len(self.new_tasks)
        elif queue == 'tasks_to_fix':
            return len(self.to_fix_tasks)
        else:
            return len(self.done_tasks)


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty('new_tasks'))  # Проверяем очередь новых задач

    # помещаем объекты в очередь новых задач
    qc_obj.todo_queue('Разработать программу распределения очередей')
    qc_obj.todo_queue('Разработать программу выполнения задач')
    qc_obj.todo_queue('Разработать отдельную очередь для хотфиксов')

    print(qc_obj.is_empty('new_tasks'))  # -> Проверяем очередь новых задач. Непустая

    print(f"В очереди новых задач: {qc_obj.size('new_tasks')}")  # Проверяем размер очереди новых задач
    print(f"В очереди задач для доработки: {qc_obj.size('tasks_to_fix')}")  # Проверяем размер очереди задач для
    # доработки
    print(f"В очереди выполненных задач: {qc_obj.size('done_tasks')}")  # Проверяем размер очереди выполненных задач

    print(f"Задачи из очереди новых задач: {qc_obj.new_tasks}")  # Выводим список новых задач

    print("++++++++++++++Перенос 2 задач между очередями+++++++++++++++++++++++++++++++++++++++")

    qc_obj.move_between_queue('new_tasks')  # Переносим одну задачу из новых задач в выполненные
    qc_obj.move_between_queue('to_fix_tasks')  # Переносим одну задачу из новых задач в задачи для корректировки

    print(f"Задачи из очереди новых задач: {qc_obj.new_tasks}")  # Выводим список новых задач
    print(f"Задачи из очереди на корректировку: {qc_obj.to_fix_tasks}")  # Выводим список задач для корректировки
    print(f"Выполненные задачи: {qc_obj.done_tasks}")  # Выводим список выполненных задач

    print(f"В очереди новых задач: {qc_obj.size('new_tasks')}")  # Проверяем размер очереди новых задач
    print(f"В очереди задач для доработки: {qc_obj.size('tasks_to_fix')}")  # Проверяем размер очереди задач для
    # доработки
    print(f"В очереди выполненных задач: {qc_obj.size('done_tasks')}")  # Проверяем размер очереди выполненных задач

    print("+++++++++++++++++Перенос 1 задачи из очереди корректировки в выполненные +++++++++++++++++++++++++++")

    qc_obj.move_between_queue('from_fix_tasks')  # Переносим одну задачу из задач для корректировки в выполненные

    print(f"Задачи из очереди новых задач: {qc_obj.new_tasks}")  # Выводим список новых задач
    print(f"Задачи из очереди на корректировку: {qc_obj.to_fix_tasks}")  # Выводим список задач для корректировки
    print(f"Выполненные задачи: {qc_obj.done_tasks}")  # Выводим список выполненных задач

    print(f"В очереди новых задач: {qc_obj.size('new_tasks')}")  # Проверяем размер очереди новых задач
    print(f"В очереди задач для доработки: {qc_obj.size('tasks_to_fix')}")  # Проверяем размер очереди задач для
    # доработки
    print(f"В очереди выполненных задач: {qc_obj.size('done_tasks')}")  # Проверяем размер очереди выполненных задач
