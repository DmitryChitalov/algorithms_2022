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


class Task_board:

    def __init__(self):
        self.task = []
        self.task_remake = []
        self.task_completed = []
        # Действия
        self.completed = 1
        self.remake = 2

    def basic_task(self, task):
        for i in task:
            print(task)
            self.task.append(i)
            test = (int(input("Задача решена?(Если да введите 1, Если нет введите 2) : ")))
            if test == self.completed:
                print(f"Задача - {task} = Выполнена")
                self.task_completed.append(i)
                self.task.pop()
            elif test == self.remake:
                print(f"Задача - {task} = Отправленно на доработку")
                self.task_remake.append(i)
                self.task.pop()

    def for_revision(self, task):
        for i in self.task_remake:
            print(f" Задачи на доработке {self.task_remake}")
            print(f" Корректировка задачи - {task}")
            test = (int(input("Задачу нужно изменить ? (Если да введите 1, Если нет введите 2) : ")))
            if test == self.completed:
                self.task_remake.pop()
                self.task.append(task)
            elif test == self.remake:
                continue

    def report_task(self):
        print(f" Список выполненых задач: {self.task_completed}")
        print(f" Список текущих задач: {self.task}")
        print(f" Список задач на доработке: {self.task_remake}")


if __name__ == "__main__":
    board = Task_board()
    # задачи
    board.basic_task(["купить 10м белого фона"])
    board.basic_task(["купить 4 лампы для источника"])
    board.for_revision(["купить 7 ламп для источника"])
    board.report_task()

