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
        self.base = []
        self.modi = []
        self.cmpl = []

    def base_in(self, item):
        self.base.insert(0, item)

    def mod_task(self):
        task = self.base.pop()
        self.modi.insert(0, task)

    def done_mod_task(self):
        task = self.modi.pop()
        self.cmpl.append(task)  # В списке решенных задач специально не стал пользоваться fifo.

    def done_task(self):
        task = self.base.pop()
        self.cmpl.append(task)  # В списке решенных задач специально не стал пользоваться fifo.


if __name__ == '__main__':
    TB_test = TaskBoard()
    TB_test.base_in(1)
    TB_test.base_in(2)
    TB_test.base_in(3)
    TB_test.base_in(4)
    TB_test.base_in(5)
    TB_test.mod_task()
    TB_test.mod_task()
    TB_test.done_mod_task()
    TB_test.done_task()

    print(TB_test.base)
    print(TB_test.modi)
    print(TB_test.cmpl)
