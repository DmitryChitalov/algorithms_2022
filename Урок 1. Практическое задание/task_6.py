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
    def __init__(self, name='Task_Board'):
        self.__name = name
        print(f'{self.__name} created!')
        self.__main_tasks = []
        self.__tasks_for_improvement = []
        self.__completed_tasks = []

    def __str__(self):
        return f'Main tasks: {self.__main_tasks}\n' \
               f'Tasks for improvements: {self.__tasks_for_improvement}\n' \
               f'Completed tasks: {self.__completed_tasks}'

    def add_main_task(self, *args):
        for task_name in args:
            self.__main_tasks.insert(0, task_name)

    def give_main_task(self):
        try:
            return self.__main_tasks.pop()
        except IndexError as err:
            print(err)

    def give_task_for_improv(self):
        try:
            return self.__tasks_for_improvement.pop()
        except IndexError as err:
            print(err)

    def show_completed_tasks(self):
        return self.__completed_tasks

    def switch_main_to_completed(self, *args):
        for task_name in args:
            if task_name in self.__main_tasks:
                self.__completed_tasks.insert(0, task_name)
                self.__main_tasks.remove(task_name)
            elif task_name in self.__tasks_for_improvement:
                self.__completed_tasks.insert(0, task_name)
                self.__tasks_for_improvement.remove(task_name)

    def switch_to_improvement(self, *args):
        for task_name in args:
            if task_name in self.__main_tasks:
                self.__tasks_for_improvement.insert(0, task_name)
                self.__main_tasks.remove(task_name)
            if task_name in self.__completed_tasks:
                self.__tasks_for_improvement.insert(0, task_name)
                self.__completed_tasks.remove(task_name)


if __name__ == '__main__':
    task_board = TaskBoard('MyBoard')
    task_board.add_main_task('Buy products', 'Go to school', 'Buy books')
    print(task_board)
    task_board.switch_main_to_completed('Buy products', 'Go to school')
    task_board.switch_to_improvement('Buy products', 'Buy books')
    task_board.add_main_task('Leave home')
    print(task_board)
    print(task_board.give_main_task())
    print(task_board.give_task_for_improv())
