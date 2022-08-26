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
    def __init__(self):  # Создаём класс "Доска задач" из трёх очередей
        self.elems = [['Базовые'], ['Доработка'], ['Решённые']]

    def is_empty(self, queve_name):  # Проверяем, есть ли задачи на "Доске задач" в конкретных очередях
        if queve_name == 'Базовые' and len(self.elems[0]) == 1:
            return True
        elif queve_name == 'Доработка' and len(self.elems[1]) == 1:
            return True
        elif queve_name == 'Решённые' and len(self.elems[2]) == 1:
            return True
        elif queve_name == 'Все' and len(self.elems[0]) == 1 and len(self.elems[1]) == 1 and len(self.elems[2]) == 1:
            return True
        else:
            return False

    def to_queue(self, item, queve_name):  # Помещаем объекты в очереди
        if queve_name == 'Базовые':
            return self.elems[0].insert(1, item)
        elif queve_name == 'Доработка':
            return self.elems[1].insert(1, item)
        elif queve_name == 'Решённые':
            return self.elems[2].insert(1, item)

    def show_all(self):  # Просматриваем содержимое "Доски задач"
        return self.elems

    def from_queue(self, queve_name):  # Просмотр очередных задач в очередях и принятие решения
        if queve_name == 'Базовые':
            if len(self.elems[0]) > 1:
                print('Отправить на доработку - нажмите 1, отправить в решённые - 2')
                decision = input(self.elems[0][-1])
                if decision == '1':
                    self.elems[1].insert(1, self.elems[0].pop())
                    return 'Задача отправлена на доработку'
                elif decision == '2':
                    self.elems[2].insert(1, self.elems[0].pop())
                    return 'Задача отправлена в решённые'
                else:
                    return 'Задача оставлена в списке Базовых'
            else:
                return 'Список пуст'
        elif queve_name == 'Доработка':
            if len(self.elems[1]) > 1:
                print('Отправить в базовые - нажмите 1, отправить в решённые - 2')
                decision = input(self.elems[1][-1])
                if decision == '1':
                    self.elems[0].insert(1, self.elems[1].pop())
                    return 'Задача отправлена в базовые'
                elif decision == '2':
                    self.elems[2].insert(1, self.elems[1].pop())
                    return 'Задача отправлена в решённые'
                else:
                    return 'Задача оставлена для доработки'
            else:
                return 'Список пуст'
        elif queve_name == 'Решённые':
            if len(self.elems[2]) > 1:
                print('Отправить в базовые - нажмите 1, отправить на доработку - 2')
                decision = input(self.elems[2][-1])
                if decision == '1':
                    self.elems[0].insert(1, self.elems[2].pop())
                    return 'Задача отправлена в базовые'
                elif decision == '2':
                    self.elems[1].insert(1, self.elems[2].pop())
                    return 'Задача отправлена на доработку'
                else:
                    return 'Задача решена'
            else:
                return 'Список пуст'


if __name__ == '__main__':
    qc_obj = QueueClass()

    print(qc_obj.is_empty('Базовые'))  # -> True. Очередь Базовых задач пуста
    print(qc_obj.is_empty('Доработка'))  # -> True. Очередь задач на Доработку пуста
    print(qc_obj.is_empty('Решённые'))  # -> True. Очередь Решённых задач пуста
    print(qc_obj.is_empty('Все'))  # -> True. Все очереди пусты

    # помещаем объекты в очереди
    qc_obj.to_queue('Задача_1', 'Базовые')
    qc_obj.to_queue('Задача_2', 'Базовые')
    qc_obj.to_queue('Задача_3', 'Доработка')
    qc_obj.to_queue('Задача_4', 'Доработка')
    qc_obj.to_queue('Задача_5', 'Решённые')
    qc_obj.to_queue('Задача_6', 'Решённые')

    print(qc_obj.is_empty('Базовые'))  # -> False. Очередь Базовых задач не пуста
    print(qc_obj.is_empty('Доработка'))  # -> False. Очередь задач на Доработку не пуста
    print(qc_obj.is_empty('Решённые'))  # -> False. Очередь Решённых задач не пуста
    print(qc_obj.is_empty('Все'))  # -> False. Все очереди не пусты

    # Просматриваем содержимое "Доски задач"
    print(qc_obj.show_all())

    # Просмотр очередных задач в очередях и принятие решения
    print(qc_obj.from_queue('Доработка'))
    print(qc_obj.from_queue('Доработка'))
    print(qc_obj.from_queue('Доработка'))
    print(qc_obj.from_queue('Доработка'))

    # Просматриваем содержимое "Доски задач"
    print(qc_obj.show_all())
