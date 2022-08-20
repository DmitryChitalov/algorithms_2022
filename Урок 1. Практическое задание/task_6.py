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
import random

class Queue:
    def __init__(self):
        self.number = 1
        self.queue_base = []
        self.queue_modify = []
        self.queue_complete = []
        
    def queue_add(self):
        self.queue_base.append(self.number)
        self.number += 1
        if (len(self.queue_base) > 3):
            if(random.random() < 0.5):
                self.queue_modify.append(self.queue_base.pop(0))
                
                if(len(self.queue_modify) > 3):
                    self.queue_complete.append(self.queue_modify.pop(0))
                
            else:
                self.queue_complete.append(self.queue_base.pop(0))
                
        print("base:", self.queue_base)
        print("modify:", self.queue_modify)
        print("complete:", self.queue_complete)
        
        
a = Queue()

a.queue_add()
a.queue_add()
a.queue_add()
a.queue_add()
a.queue_add()
a.queue_add()
a.queue_add()
a.queue_add()
a.queue_add()
a.queue_add()
a.queue_add()
a.queue_add()
