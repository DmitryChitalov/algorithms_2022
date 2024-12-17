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
from collections import deque


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.status = 'New'  # Статус задачи: New, In Progress, Done, Under Review

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status})"


class TaskBoard:
    def __init__(self):
        self.base_queue = deque()  # Базовая очередь
        self.review_queue = deque()  # Очередь на доработку
        self.completed_tasks = []  # Список решенных задач

    def add_task(self, task):
        """Добавить задачу в базовую очередь."""
        self.base_queue.append(task)

    def start_task(self):
        """Начать работу над задачей из базовой очереди."""
        if self.base_queue:
            task = self.base_queue.popleft()
            task.status = 'In Progress'
            print(f"Задача '{task.title}' начата.")
            return task
        else:
            print("Нет доступных задач в базовой очереди.")
            return None

    def complete_task(self, task):
        """Завершить задачу и отправить в список решенных задач."""
        if task:
            task.status = 'Done'
            self.completed_tasks.append(task)
            print(f"Задача '{task.title}' решена.")
        else:
            print("Задача не была начата.")

    def send_for_review(self, task):
        """Отправить задачу на доработку."""
        if task:
            task.status = 'Under Review'
            self.review_queue.append(task)
            print(f"Задача '{task.title}' отправлена на доработку.")

    def resolve_reviewed_task(self):
        """Переместить задачу из очереди на доработку в решенные задачи."""
        if self.review_queue:
            task = self.review_queue.popleft()
            task.status = 'Done'
            self.completed_tasks.append(task)
            print(f"Задача '{task.title}' после доработки решена.")
        else:
            print("Нет задач на доработку.")

    def show_status(self):
        """Показать статус доски задач."""
        print("\nСтатус доски задач:")
        print("Базовая очередь:", list(self.base_queue))
        print("Очередь на доработку:", list(self.review_queue))
        print("Решенные задачи:", self.completed_tasks)


# Пример использования:
if __name__ == "__main__":
    task_board = TaskBoard()

    # Добавляем задачи на доску
    task_board.add_task(Task("Задача 1", "Описание задачи 1"))
    task_board.add_task(Task("Задача 2", "Описание задачи 2"))
    task_board.add_task(Task("Задача 3", "Описание задачи 3"))

    # Начинаем работу над задачами
    task1 = task_board.start_task()  # Начать задачу 1
    task2 = task_board.start_task()  # Начать задачу 2

    # Завершаем одну задачу и отправляем другую на доработку
    task_board.complete_task(task1)
    task_board.send_for_review(task2)

    # Завершаем задачу после доработки
    task_board.resolve_reviewed_task()

    # Показываем текущий статус доски задач
    task_board.show_status()
