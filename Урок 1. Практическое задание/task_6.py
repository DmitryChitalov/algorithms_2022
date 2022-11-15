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


class TaskDesk:
    def __init__(self):
        self.main_tasks = []
        self.working_tasks = []
        self.decided_tasks = []

    def to_main(self, task):
        self.main_tasks.insert(0, task)

    def to_work(self):
        try:
            task = self.main_tasks.pop()
            self.working_tasks.insert(0, task)
        except IndexError:
            print('no main tasks')

    def main_to_decided(self):
        try:
            task = self.main_tasks.pop()
            self.decided_tasks.insert(0, task)
        except IndexError:
            print('no main tasks')

    def work_to_decided(self):
        try:
            task = self.working_tasks.pop()
            self.decided_tasks.insert(0, task)
        except IndexError:
            print('no working tasks')

    def from_desk(self):
        try:
            self.decided_tasks.pop()
        except IndexError:
            print('no decided tasks')

    def size(self, main=None, work=None, decide=None):
        if main:
            return len(self.main_tasks)
        elif work:
            return len(self.working_tasks)
        elif decide:
            return len(self.decided_tasks)
        else:
            return len(self.main_tasks) + len(self.working_tasks) + len(self.decided_tasks)

    def is_empty(self, main=None, work=None, decide=None):
        if main:
            return len(self.main_tasks) == 0
        elif work:
            return len(self.working_tasks) == 0
        elif decide:
            return len(self.decided_tasks) == 0
        else:
            return (len(self.main_tasks) + len(self.working_tasks) + len(self.decided_tasks)) == 0

    def show_desk(self):
        print(f'm - {self.main_tasks}\n'
              f'w - {self.working_tasks}\n'
              f'd - {self.decided_tasks}\n')


if __name__ == '__main__':

    # Далее проверки
    my_desk = TaskDesk()
    print(my_desk.size())
    print(my_desk.is_empty())

    a = 69
    i = 1
    while i < 6:
        t = chr(a)
        my_desk.to_main(t)
        i = i + 1
        a = a - 1

    my_desk.show_desk()

    my_desk.main_to_decided()
    my_desk.main_to_decided()
    my_desk.to_work()
    my_desk.to_work()
    my_desk.show_desk()

    my_desk.from_desk()
    my_desk.work_to_decided()
    my_desk.show_desk()

    print(my_desk.size(decide=True))
