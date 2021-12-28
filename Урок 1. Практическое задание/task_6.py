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
from datetime import datetime
print(datetime.now())

class TaskBoard:

    def __init__(self):
        self.base = []
        self.revision = []
        self.done = []

    def add_task(self, name, desc, status, date = datetime.now()):
        if status == 'base':
            self.base.append({'name': name, 'desc': desc, 'date': date})
        elif status == 'revision':
            self.revision.append({'name': name, 'desc': desc, 'date': date})
        else:
            print('Аргумент status должен быть равен либо revision, либо base.')

    def into_done(self, name):
        into_done_trigger = False

        for base_item, revision_item in zip(enumerate(self.base), enumerate(self.revision)):
            if base_item[1]['name'] == name:
                into_done_trigger = True
                self.done.append(base_item[1])
                del self.base[base_item[0]]
                break
            elif revision_item[1]['name']:
                into_done_trigger = True
                self.done.append(revision_item[1])
                del self.revision[revision_item[0]]
                break

        if not into_done_trigger:
            print('Не существует данной задачи!')

    def into_revision(self, name):
        into_revision_trigger = False

        for base_item, done_item in zip(enumerate(self.base), enumerate(self.done)):
            if base_item[1]['name'] == name:
                into_revision_trigger = True
                self.revision.append(base_item[1])
                del self.base[base_item[0]]
                break
            elif done_item[1]['name']:
                into_revision_trigger = True
                self.revision.append(done_item[1])
                del self.done[base_item[0]]
                break

        if not into_revision_trigger:
            print('Не существует данной задачи!')

    def show_all_tasks(self):
        return f'{self.base}\n{self.revision}\n{self.done}'

trello = TaskBoard()

trello.add_task('hello world', 'hello world', 'base')
trello.add_task('2nd prog', '2nd prog', 'revision')
trello.add_task('3nd prog', '3nd prog', 'revision')
trello.into_done('3nd prog')

print(trello.show_all_tasks())
