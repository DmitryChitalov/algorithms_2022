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
        self.basic = []
        self.moderate = []
        self.finished = []

    def new_task(self, task):
        """
        Новая задача добавляется в базовую очерель
        """
        self.basic.insert(0, task)

    def from_basic(self):
        """
        Берет задачу из основной
        :return: возвращает ее
        """
        if self.basic:
            return self.basic.pop()

    def from_moderate(self):
        """
        берет задачу из очереди на доработку
        и возвращает ее
        """
        if self.moderate:
            return self.moderate.pop()

    def to_moderate(self):
        """
        Берет задачу из
        """
        self.moderate.insert(0, self.from_basic())

    def to_finished(self, queue: int):
        """
        Принимает на вход очередь в виде числа 1 или 2
        1 - из базовой очереди
        2 - из очереди на доработку
        в заисимости от цифры берет задачу из нужной очереди
        """
        if queue == 1:
            self.finished.insert(0, self.from_basic())
        elif queue == 2:
            self.finished.insert(0, self.from_moderate())
        else:
            print('Queue Error')

    def basic_to_finished(self):
        self.finished.insert(0, self.from_basic())

    def moderate_to_finished(self):
        self.finished.insert(0, self.moderate.pop())

    def __str__(self):
        text = f"Tasks in Basic : {self.basic}\n" \
               f"Tasks in Moderate : {self.moderate}\n" \
               f"Tasks in Finished : {self.finished}\n"
        return text


if __name__ == '__main__':
    desk = TaskDesk()
    desk.new_task('Wash Car')
    desk.new_task('Visit Father')
    desk.new_task('Finish Lesson 1')
    desk.new_task('Watch lesson 2')
    desk.to_finished(1)
    desk.to_moderate()
    desk.to_moderate()
    print(desk)
    desk.to_finished(2)
    desk.to_finished(2)
    desk.to_finished(2)

    print(desk)
