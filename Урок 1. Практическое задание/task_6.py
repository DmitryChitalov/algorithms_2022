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
class Task_board():
    """FIFO"""
    def __init__(self, default_tasks=None):
        self.tasks = {
            "current" : [],
            "to_solve": [],
            "solved": [],
        }
        self.fill_tasks(default_tasks)

    def from_current(self):
        return self.tasks["current"].pop()

    def from_solve(self):
        return self.tasks["to_solve"].pop()

    def from_solved(self):
        return self.tasks["solved"].pop()

    def to_current(self, task):
        self.tasks["current"].insert(0, task)

    def to_solve(self, task):
        self.tasks["to_solve"].insert(0, task)

    def to_solved(self, task):
        self.tasks["solved"].insert(0, task)

    def fill_tasks(self, tasks_arr: list):
        if type(tasks_arr) == list:
            self.tasks["current"].extend(tasks_arr)

    @property
    def show_all_tasks(self):
        return self.tasks.items()


if __name__ == "__main__":
    """ Инициализация """
    tasks = ["new year", "test scripts", "buy new cup", "run git init", "take over the world until 2023",
             "mystery task from 1999", "clear browser history"]
    board =Task_board(tasks)

    #[print(f"{x}: {y}") for x, y in board.show_all_tasks]
    additional_tasks = ["run code", "enjoy python programming"]
    board.fill_tasks(additional_tasks)

    [print(f"{x}: {y}") for x,y in board.show_all_tasks]
    """ Проверка """
    print("*" * 40)
    board.to_solve(board.from_current())
    board.to_solved(board.from_current())
    board.to_solved(board.from_current())
    board.to_current(board.from_solved())
    [print(f"{x}: {y}") for x, y in board.show_all_tasks]