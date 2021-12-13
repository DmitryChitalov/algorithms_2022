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


class TaskDesk:
    """"""
    def __init__(self):
        self._tasks = []
        self._done = []
        self._correct = []

    def add_task(self, task):
        self._tasks.insert(0, task)

    def ch_task(self, key):
        """Метод для базовых тасков
        key = 1 - Добавить в готовые таски
        key = anykey - Добавить в доработки
        """
        if len(self._tasks) == 0:
            return None
        return self._done.insert(0, self._tasks.pop()) if key == 1 else \
            self._correct.insert(0, self._tasks.pop())

    def ch_done(self, key):
        """Метод для решенных тасков
        key = 1 - Добавить в доработки
        key = anykey - Добавить в базовые таски
        """
        if len(self._done) == 0:
            return None
        return self._correct.insert(0, self._done.pop()) if key == 1 else \
            self._tasks.insert(0, self._done.pop())

    def ch_correct(self, key):
        """Метод для решенных тасков
        key = 1 - Добавить в решеные
        key = anykey - Добавить в базовые таски
        """
        if len(self._correct) == 0:
            return None
        return self._done.insert(0, self._correct.pop()) if key == 1 else \
            self._tasks.insert(0, self._correct.pop())

    def get_len(self):
        return f'Сейчас задач - {len(self._tasks)}\nРешенных - {len(self._done)}\n' \
               f'На доработке - {len(self._correct)}'

    def get_last_task(self):
        return self._tasks[-1] if len(self._tasks) > 0 else None

    def get_last_done(self):
        return self._done[-1] if len(self._done) > 0 else None

    def get_last_correct(self):
        return self._correct[-1] if len(self._correct) > 0 else None


test = TaskDesk()
test.add_task('test1')
test.add_task('test2')
test.ch_task(1)
test.ch_task(2)
print(test.get_len())
print(test.get_last_task())


