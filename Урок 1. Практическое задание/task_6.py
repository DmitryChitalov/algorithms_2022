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

class Tasks:

    def __init__(self):
        self.tasks = []
        self.modification = []
        self.solved = []

    def push_in_task(self, el):
        return self.tasks.append(el)

    def push_in_modification(self, el):
        self.tasks.remove(el)
        return self.modification.append(el)

    def push_in_solved(self, el):
        if el in self.tasks:
            self.tasks.remove(el)
        elif el in self.modification:
            self.modification.remove(el)
        else:
            self.solved.append(el)
        return self.solved.append(el)

    def see_tascks(self):
        return [i for i in self.tasks]

    def see_modification(self):
        return [i for i in self.modification]

    def see_solved(self):
        return [i for i in self.solved]


task = ['Купить молока', 'Помыть посуду', 'Выгулять собаку', 'Решить задачки']




tmp = Tasks()
for i in task:
    tmp.push_in_task(i)
print(tmp.see_tascks())
good = 'Купить молока'
if good in tmp.see_tascks():
    tmp.push_in_modification(good)
print(tmp.see_tascks())
print(tmp.see_modification())
good_2 = 'Помыть посуду'
if good_2 in tmp.see_tascks():
    tmp.push_in_solved(good_2)
print(tmp.see_tascks())
print(tmp.see_solved())
if good in tmp.see_modification():
    tmp.push_in_solved(good)
print(tmp.see_tascks())
print(tmp.see_solved())
print(tmp.see_modification())









