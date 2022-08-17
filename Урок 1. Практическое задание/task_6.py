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


class TaskBoard:
    def __init__(self):
        self.main_board, self.main_task_id = [], 0
        self.revision_board, self.revision_task_id = [], 0
        self.solved_board, self.solved_task_id = [], 0

    def main_board_is_empty(self):
        return self.main_task_id == 0

    def revision_board_is_empty(self):
        return self.revision_task_id == 0

    def show_board(self):
        return self.main_board, self.revision_board, self.solved_board

    def add_new_task(self, task):
        self.main_board.insert(0, [self.main_task_id, task])
        self.main_task_id += 1

    def solved(self):
        self.main_task_id -= 1
        self.solved_board.insert(0, self.main_board[self.main_task_id])
        self.main_board.pop()
        self.solved_task_id += 1

    def revision_solved(self):
        self.revision_task_id -= 1
        self.solved_board.insert(0, self.revision_board[self.revision_task_id])
        self.main_task_id += 1

    def to_revision(self):
        self.solved_task_id -= 1
        self.revision_board.insert(0, self.solved_board[self.solved_task_id])
        self.revision_task_id += 1


if __name__ == '__main__':
    board1 = TaskBoard()
    board1.add_new_task('тестовая задача')
    print(board1.show_board())
    board1.solved()
    print(board1.show_board())
