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


class Queue:
    def __init__(self):
        self.lst = []
    
    def push(self, value):
        self.lst.insert(0, value)
    
    def from_queue(self):
        return self.lst.pop()

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, n):
        return self.lst[n]
    

class TaskBoard:
    def __init__(self):
        self.base = Queue()
        self.rework = Queue()
        self.log = []
    
    def add_task(self, task):
        self.base.push(task)

    def close_task(self):
        task = self.base.from_queue()
        self.log.append(task)

    def to_rework(self):
        task = self.base.from_queue()
        self.rework.push(task)

    def from_rework(self):
        task = self.rework.from_queue()
        self.base.push(task)

    def get_last_task(self):
        return self.base[len(self.base) - 1]

    def get_all_base(self):
        return self.base.lst

    def get_all_rework(self):
        return self.rework.lst


if __name__ == '__main__':
    print('***Create taskboard, add 3 tasks')
    test_taks_board = TaskBoard()
    test_taks_board.add_task('Task #1')
    test_taks_board.add_task('Task #2')
    test_taks_board.add_task('Task #3')
    
    print('All tasks:', test_taks_board.get_all_base())
    print('Last:', test_taks_board.get_last_task())

    print('***Add to rework')
    test_taks_board.to_rework()
    print('All rework:', test_taks_board.get_all_rework())
    print('All tasks:', test_taks_board.get_all_base())
    print('Last:', test_taks_board.get_last_task())

    print('***Close task')
    test_taks_board.close_task()
    print('All rework:', test_taks_board.get_all_rework())
    print('All tasks:', test_taks_board.get_all_base())
    print('Last:', test_taks_board.get_last_task())

    print('***Move from rework')
    test_taks_board.from_rework()
    print('All rework:', test_taks_board.get_all_rework())
    print('All tasks:', test_taks_board.get_all_base())
    print('Last:', test_taks_board.get_last_task())