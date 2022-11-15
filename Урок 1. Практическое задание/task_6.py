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

class TaskBoard(object):
    """ Класс создаёт объекты содержащие списки задач
        на выполнение, корректировку и список выполненных
        задач.

    Methods:
        new_task        -> None: Добавляет новую задачу в начало списка 'tasks'.
        to_complited    -> None: Перемещает элемент из конца списка 'tasks' в начало списка 'completed'.
        to_corrected    -> None: Перемещает элемент из конца списка 'tasks' в начало списка 'corrected'.
        corrected_to_complited -> None: Перемещает элемент из конца списка 'corrected' в начало списка 'completed'.
        clear_board     -> None: Очищает списки задач.
    """

    __slots__ = ('tasks', 'completed', 'corrected')

    def __init__(self) -> None:
        self.tasks = list()
        self.completed = list()
        self.corrected = list()

    def __is_empty(self, source: list) -> None:
        # Проверить список 'source' на пустоту
        return source == []

    def __move_task(self, source: list, destination: list) -> None:
        # Переместить последний элемент списка 'source' в начало списка 'destination'.
        if self.__is_empty(source=source):
            print('Source is empty.')
        else:
            destination.insert(0, source.pop())

    def new_task(self, task: str) -> None:
        # Добавить новую задачу в начало списка 'tasks'.
        self.tasks.insert(0, task)

    def to_complited(self) -> None:
        # Переместить элемент из конца списка 'tasks' в начало списка 'completed'.
        self.__move_task(source=self.tasks, destination=self.completed)

    def to_corrected(self) -> None:
        # Переместить элемент из конца списка 'tasks' в начало списка 'corrected'.
        self.__move_task(source=self.tasks, destination=self.corrected)

    def corrected_to_complited(self) -> None:
        # Переместить элемент из конца списка 'corrected' в начало списка 'completed'.
        self.__move_task(source=self.corrected, destination=self.completed)

    def clear_board(self) -> None:
        # Очистить списки задач
        for item in [self.tasks, self.completed, self.corrected]:
            item.clear()
        print('Board was successfully cleared!')

    def __str__(self) -> str:
        return f'New tasks: {self.tasks}\nCorrected tasks: {self.corrected}\nComplited tasks: {self.completed}'

if __name__ == '__main__':
    
    board = TaskBoard()
    board.to_complited()

    for number in range(15):
        board.new_task(f'Task {number}')
    print(board)

    for _ in range(5):
        board.to_corrected()
        board.to_complited()
    print(board)

    for _ in range(5):
        board.to_complited()
        board.corrected_to_complited()
    print(board)

    board.clear_board()
    print(board)