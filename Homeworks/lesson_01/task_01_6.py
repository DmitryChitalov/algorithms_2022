"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие нескольких очередей задач, например:
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TackBoardClass:
    def __init__(self):
        self.inbox = []
        self.revision = []
        self.complete = []

    def inbox_is_empty(self):
        return self.inbox == []

    def revision_is_empty(self):
        return self.revision == []

    def complete_is_empty(self):
        return self.complete == []

    def inbox_view(self):
        print(self.inbox)

    def revision_view(self):
        print(self.revision)

    def complete_view(self):
        print(self.complete)

    def to_inbox(self, task):
        self.inbox.insert(0, task)

    def from_inbox_to_revision(self):
        if len(self.inbox) == 0:
            print('Нет входящих задач.')
        else:
            self.revision.insert(0, self.inbox[-1])
            del self.inbox[-1]

    def from_inbox_to_complete(self):
        if len(self.inbox) == 0:
            print('Нет входящих задач.')
        else:
            self.complete.insert(0, self.inbox[-1])
            del self.inbox[-1]

    def from_revision_to_complete(self):
        if len(self.revision) == 0:
            print('Нет задач на доработку.')
        else:
            self.complete.insert(0, self.revision[-1])
            del self.revision[-1]


if __name__ == '__main__':

    TBC_obj = TackBoardClass()

    print(TBC_obj.inbox_is_empty())
    print(TBC_obj.revision_is_empty())
    print(TBC_obj.complete_is_empty())

    for i in range(1, 6):
        TBC_obj.to_inbox(f'Task {i}')

    TBC_obj.inbox_view()
    print(TBC_obj.inbox_is_empty())

    for i in range(2):
        TBC_obj.from_inbox_to_revision()

    TBC_obj.inbox_view()
    TBC_obj.revision_view()
    print(TBC_obj.revision_is_empty())

    for i in range(2):
        TBC_obj.from_inbox_to_complete()

    TBC_obj.inbox_view()
    TBC_obj.complete_view()
    print(TBC_obj.complete_is_empty())

    for i in range(2):
        TBC_obj.from_inbox_to_revision()

    TBC_obj.revision_view()
    print(TBC_obj.inbox_is_empty())

    for i in range(4):
        TBC_obj.from_revision_to_complete()

    TBC_obj.complete_view()
