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


class Board():

    def __init__(self):
        self.columns = {
            'basic': [],
            'remake': [],
            'done': []
        }

    def add_task(self, column, task):
        """Добавить задачу в колонку"""
        self.columns[column].insert(0, task)

    def get_task(self, column):
        """Забрать задачу из колонки"""
        return self.columns[column].pop()

    @property
    def get_columns(self):
        """Посмотреть состояние доски"""
        return self.columns


if __name__ == '__main__':
    my_board = Board()

    task_1 = 'Первая фича'
    task_2 = 'Вторая фича'
    task_3 = 'Третья фича'

    my_board.add_task('basic', task_1)
    my_board.add_task('basic', task_2)
    my_board.add_task('basic', task_3)
    print(my_board.get_columns)

    moving_task = my_board.get_task('basic')
    my_board.add_task('remake', moving_task)
    print(my_board.get_columns)

    moving_task = my_board.get_task('basic')
    my_board.add_task('done', moving_task)
    print(my_board.get_columns)

    moving_task = my_board.get_task('remake')
    my_board.add_task('done', moving_task)
    print(my_board.get_columns)
