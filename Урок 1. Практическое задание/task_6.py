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


class QueueClass:
    def __init__(self):
        self.basic = []
        self.finished = []
        self.not_finished = []

    def to_basic_queue(self, item):
        self.basic.insert(0, item)

    def from_basic_to_finished(self):
        self.finished.insert(0, self.basic.pop())

    def from_basic_to_not_finished(self):
        self.not_finished.insert(0, self.basic.pop())

    def show_basic_queue(self):
        return self.basic

    def show_finished_queue(self):
        return self.finished

    def show_not_finished_queue(self):
        return self.not_finished


if __name__ == '__main__':
    Desc = QueueClass()

    # заполняем базовую очередь
    Desc.to_basic_queue('первый')
    Desc.to_basic_queue('второй')
    Desc.to_basic_queue('третий')
    Desc.to_basic_queue('четвертый')

    # проверяем заполненность
    print(f'список задач: {Desc.show_basic_queue()}')

    Desc.from_basic_to_finished()  # распределяем задачи по местам
    Desc.from_basic_to_finished()
    Desc.from_basic_to_not_finished()

    print(f'Решенные задачи: {Desc.show_finished_queue()}')  # проверка очередей
    print(f'Оставшиеся задачи: {Desc.show_basic_queue()}')
    print(f'Задачи на доработку: {Desc.show_not_finished_queue()}')
