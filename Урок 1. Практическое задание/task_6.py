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
        self.new_elems=[]

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)


    def from_queue(self,status):
        if status=='Yes':
            return self.elems.pop()
        elif status=='No':
            self.elems.pop()
            self.new_elems.insert(0,self)

    def size(self):
        return len(self.elems)
    def size2(self):
        return len(self.new_elems)
task=QueueClass()
task.to_queue('сделать уборку')
task.to_queue('позвонить маме')
print(task.is_empty())
task.from_queue('No')
print(task.size2())