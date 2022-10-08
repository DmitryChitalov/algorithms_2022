"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.base = []
        self.work = []
        self.res = []

    def is_empty(self):
        return self.base == []

    def to_base(self, item):
        self.base.insert(0, item)

    def from_base(self):
        return self.base.pop()

    def to_res(self, item):
        self.res.insert(0, item)

    def to_work(self, item):
        self.work.insert(0, item)

    def size_base(self):
        return len(self.base)

    def curr_task(self):
        return self.base[-1]                # разобраться со срезом. Ошибка, чтобы правильно выводило название задачи

    def get_base(self):
        return self.base

    def get_res(self):
        return self.res

    def get_work(self):
        return self.work


if __name__ == '__main__':

    def task_manager(tasks):

        qc_obj = QueueClass()

        for j in range(len(tasks)):
            qc_obj.to_base(tasks[j])
            # print(qc_obj.get_base())

        while qc_obj.size_base() > 0:
            meth = int(input(f'Задача {qc_obj.curr_task()}. Введите 1 - решено или 0 - на доработку: '))
            if meth == 1:
                qc_obj.to_res(qc_obj.from_base())
                # print(qc_obj.get_base())
            elif meth == 0:
                qc_obj.to_work(qc_obj.from_base())
                # print(qc_obj.get_base())
            else:
                print('Неверный ввод')

        return qc_obj.get_base(), qc_obj.get_work(), qc_obj.get_res()


    list_tasks = ['Расчет суммы', 'Подготовить договор', 'Нарисовать схему', 'Подготовить отчет', 'Проверить методичку', 'Написать письмо', ]
    print(task_manager(list_tasks))

