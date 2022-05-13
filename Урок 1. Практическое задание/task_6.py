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

class Kanban:

    def __init__(self):
        self.boards = {'base':[],'revision':[],'completed':[]}

    def get_board(self,board_name):
        return self.boards.get(board_name)

    def is_empty(self,board_name):
        return self.get_board(board_name) == []

    def to_board(self,board_name,issue):
        self.get_board(board_name).insert(0,issue)

    def from_board(self,board_name):
        return self.get_board(board_name).pop()

    def move_from_to(self,from_board,to_board):
        issue = self.from_board(from_board)
        self.to_board(to_board,issue)
        return issue

    def print_board(self,board_name):
        print(f'board {board_name}: {self.get_board(board_name)}')

if __name__ == '__main__':

    Kanban_Obj = Kanban()

    for i in range(10):
        Kanban_Obj.to_board('base',f'issue{i}')

    Kanban_Obj.print_board('base')

    for i in range(5):
        Kanban_Obj.move_from_to('base','revision')

    Kanban_Obj.print_board('base')
    Kanban_Obj.print_board('revision')

    for i in range(2):
        Kanban_Obj.move_from_to('revision','completed')

    Kanban_Obj.print_board('base')
    Kanban_Obj.print_board('revision')
    Kanban_Obj.print_board('completed')
