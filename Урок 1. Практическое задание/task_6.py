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

class QueueClass:
    def __init__(self):
        self.base = []
        self.process = []
        self.finish = []

    def is_empty(self):
        print("Список задач пуст?: ")
        return True if (self.base == []) is True \
                       and (self.process == []) is True else False

    def to_base(self, item):
        print(f" {item} - Добавлен в очередь: ")
        self.base.insert(0, item)

    def to_process(self, item):
        if item in self.base:
            val = self.base.index(item)
            self.process.insert(0, self.base.pop(val))
            print('Перенесен на доработку: ')
            return item
        elif item in self.finish:
            val2 = self.finish.index(item)
            self.process.insert(0, self.finish.pop(val2))
            print('Перенесен на доработку: ')
            return item
        else:
            return print('Задача не обнаружена')

    def to_finish(self, item):
        if item in self.base:
            val = self.base.index(item)
            self.finish.insert(0, self.base.pop(val))
            print('Перенесен в завершенные: ')
            return item
        elif item in self.process:
            val2 = self.process.index(item)
            self.finish.insert(0, self.process.pop(val2))
            print('Перенесен в завершенные: ')
            return item
        else:
            return print('Задача не обнаружена')

    def size(self, queue):
        if queue == 'base':
            print('Кол-во задач в базовой очереди: ')
            return len(self.base)
        if queue == 'process':
            print('Кол-во задач в работе: ')
            return len(self.process) + len(self.base)
        if queue == 'finish':
            print('Кол-во завершонных задач: ')
            return len(self.finish)


if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_base('my_obj')
    qc_obj.to_base(4)
    qc_obj.to_base(True)
    qc_obj.to_base('Задача1')
    qc_obj.to_base('Задача2')
    qc_obj.to_base('Задача3')

    print(qc_obj.is_empty())  # -> False. Очередь пустая

    print(qc_obj.size('base'))  # -> 3

    print(qc_obj.to_finish('my_obj'))  # -> my_obj

    print(qc_obj.size('finish'))  # -> 2

    print(qc_obj.to_process('Задача1'))
    print(qc_obj.to_process('Задача2'))

    print(qc_obj.to_finish('Задача1'))

    print(qc_obj.size('process'))


