"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""
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
from sys import getsizeof


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


class TaskBoardWithSlots:
    __slots__ = '__name', '__main_tasks', '__tasks_for_improvement', '__completed_tasks'

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
    classic = TaskBoard()
    with_slots = TaskBoardWithSlots()
    print(f'Память для хранения Task board: {getsizeof(classic)}\nДля TB with slots: {getsizeof(with_slots)}')
'''
Память для хранения Task board: 48
Для TB with slots: 64

Добавили слоты к классу, чем сэкономили память для хранении
'''