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
class Board:

    def __init__(self):
        self.boards = {'basa':[],'revision':[],'completed':[]}

    def get_board(self, board_title):
        return self.boards.get(board_title)

    def empty(self, board_title):
        return self.get_board(board_title) == []

    def in_board(self, board_title, issue):
        self.get_board(board_title).insert(0, issue)

    def from_board(self, board_title):
        return self.get_board(board_title).pop()

    def move(self, from_board, in_board):
        issue = self.from_board(from_board)
        self.in_board(in_board, issue)
        return issue

    def print_board(self, board_title):
        print(f'"Доска" {board_title}: {self.get_board(board_title)}')

if __name__ == '__main__':

    board = Board()
    
    for i in range(15):
        board.in_board('basa', f'issue{i}')

    board.print_board('basa')

    for i in range(10):
        board.move('basa','revision')

    board.print_board('basa')
    board.print_board('revision')

    for i in range(5):
        board.move('revision','completed')

    board.print_board('basa')
    board.print_board('revision')
    board.print_board('completed')
