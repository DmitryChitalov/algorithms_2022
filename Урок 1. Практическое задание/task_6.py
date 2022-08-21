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
        self.basic_q = []
        self.modification_q = []
        self.finished_q = []

    def new_task(self, task):
        self.basic_q.insert(0, task)

    def basic_to_mod(self):
        if self.basic_q:
            task = self.basic_q.pop()
            self.modification_q.insert(0, task)

    def mod_to_finish(self):
        if self.modification_q:
            task = self.modification_q.pop()
            self.finished_q.insert(0, task)

    def basic_to_finish(self):
        if self.basic_q:
            task = self.basic_q.pop()
            self.finished_q.insert(0, task)

    def __str__(self):
        text = f"{'*' * 10}\n" \
               f"Tasks in basic queue : {', '.join(self.basic_q)}\n" \
               f"Tasks in modification queue : {', '.join(self.modification_q)}\n" \
               f"Tasks in finished queue : {', '.join(self.finished_q)}\n" \
               f"{'*' * 10}\n"
        return text


if __name__ == "__main__":
    desc = TaskDesk()
    desc.new_task('Fix heroku bug')
    desc.new_task('Deploy Bot Production')
    print(desc)
    desc.basic_to_mod()
    desc.basic_to_mod()
    print(desc)
    desc.new_task('Test movin to finished')
    desc.new_task('From basic to finished')
    print(desc)
    desc.basic_to_finish()
    desc.basic_to_finish()
    desc.basic_to_finish()
    print(desc)
    desc.mod_to_finish()
    desc.mod_to_finish()
    desc.mod_to_finish()
    print(desc)