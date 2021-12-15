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
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')

        return self.elems.pop()

    def size(self):
        return len(self.elems)

    def __str__(self):
        return ', '.join(map(str, self.elems))


class TaskBoard:

    def __init__(self):
        self.boards = {
            'Поступившие': QueueClass(),
            'В работе': QueueClass(),
            'На тестировании': QueueClass(),
            'На доработку': QueueClass(),
            'Выполненные': QueueClass()
        }

    def q2q(self, name_from, name_to):
        self.boards[name_to].to_queue(self.boards[name_from].from_queue())

    def new_task(self, description):
        self.boards['Поступившие'].to_queue(description)

    def to_work(self):
        if not self.boards['На доработку'].is_empty():
            self.q2q('На доработку', 'В работе')
        else:
            self.q2q('Поступившие', 'В работе')

    def to_test(self):
        self.q2q('В работе', 'На тестировании')

    def to_rework(self):
        self.q2q('На тестировании', 'На доработку')

    def rework_to_work(self):
        self.q2q('На доработку', 'В работе')

    def task_completed(self):
        self.q2q('На тестировании', 'Выполненные')

    def show_boards(self):
        print('Текущее состояние дел:')
        for k, v in self.boards.items():
            print('Доска:', k)
            print(' Задачи:', v)
        print()


# Пример использования
if __name__ == '__main__':

    # Цель: спасти семью от жажды
    # Гипотеза: молоко должно помочь
    # Задача: купить молоко

    # Декомпозиция
    task_board = TaskBoard()
    task_board.new_task('Выйти из дома')
    task_board.new_task('Дойти до магазина')
    task_board.new_task('Купить молока')
    task_board.new_task('Вернуться целым и не вредимым')

    task_board.show_boards()

    # Запускаем на выполнение
    task_board.to_work()
    task_board.to_work()
    task_board.to_work()
    task_board.to_work()

    # Лишняя д.б. эксцепшн
    try:
        task_board.to_work()
    except ValueError as e:
        print('Что-то пошло не так по причине:', e)
        print('А нет, все норм! Так и должно быть')
        print()

    task_board.show_boards()

    # Передаем на тестирование
    task_board.to_test()
    task_board.to_test()
    task_board.to_test()
    task_board.to_test()

    task_board.show_boards()

    # Не то купил) е мае переделывай
    task_board.to_rework()
    task_board.to_rework()
    task_board.to_rework()
    task_board.to_rework()

    task_board.show_boards()

    # Снова в бой
    task_board.to_work()
    task_board.to_work()
    task_board.to_work()
    task_board.to_work()

    task_board.show_boards()

    # Чо сразу не сказала какое надо?! Вторая попытка
    task_board.to_test()
    task_board.to_test()
    task_board.to_test()
    task_board.to_test()

    task_board.show_boards()

    # Все норм!
    task_board.task_completed()
    task_board.task_completed()
    task_board.task_completed()
    task_board.task_completed()

    task_board.show_boards()
    # Задача выполнена! Гипотеза подтвердилась, цель достигнута - семья спасена.