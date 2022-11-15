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




class Task_Work:
    def __init__(self):
        self.start = []
        self.edit = []
        self.end = []

    def add_task(self, task):
        self.start.insert(0, task)

    def edit_insert(self):
        if self.start:
            task = self.start.pop()
            self.edit.insert(0, task)

    def edit_End(self):
        if self.edit:
            task = self.edit.pop()
            self.end.insert(0, task)

    def start_end(self):
        if self.start:
            task = self.start.pop()
            self.end.insert(0, task)

    def __str__(self):
        status = f"Доска задач \n\n"f"Задача в доске задач : {', '.join(self.start)}\n"f"Задача в очереди на изменение  : {', '.join(self.edit)}\n"f"Задача выполнена : {', '.join(self.end)}\n" f"\n\n"
        return status

if __name__ == "__main__":
    work = Task_Work()

    work.add_task('Сделать Скрипт python')
    work.add_task('Согласовать Дизайн')

    print(work)

    work.edit_insert()
    work.edit_insert()

    print(work)

    work.add_task('Передать на скрипт в прод')
    work.add_task('Передать рабочий скрипт в производство')

    print(work)

    work.start_end()
    work.start_end()
    work.start_end()

    print(work)

    work.edit_End()
    work.edit_End()
    work.edit_End()

    print(work)