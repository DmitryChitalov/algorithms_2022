"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
Т.е. решали задачу из первой очереди, какие-то решили правильно и 
перенесли в список решенных, а какие-то решели неправильно, 
но извлекли и перенесли в очередь на доработку?

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
from enum import Enum
import random

class Queue:
    def __init__(self):
        self.elems = []

    def put(self, item):
        self.elems.insert(0, item)

    def get(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)



class TaskBoard:
    class Parity(Enum):
        ODD = 1
        EVEN = 2
    
    def __init__(self):
        self.base = Queue()
        self.processed = Queue()
        self.fix_queue = Queue()
        self.solved = Queue()

    def some_work(self):
        cur_element = self.base.get()
        self.odd_or_even(cur_element)    

    def odd_or_even(self, cur_element):
        ODD, EVEN = self.__class__.Parity.EVEN, self.__class__.Parity.ODD
        some_times_error = random.choice([0, 1, 1])
        if (cur_element+some_times_error) % 2:
            self.processed.put((cur_element, EVEN))
        else:
            self.processed.put((cur_element, ODD))
        print(f'Работа для {cur_element=} выполнена, результат отправлен в очередь проверки')

    def check(self):
        ODD, EVEN = self.__class__.Parity.EVEN, self.__class__.Parity.ODD
        cur_element, parity = self.processed.get()
        if ( (cur_element % 2 and parity == EVEN) or
            (not (cur_element % 2) and parity == ODD) ):
            print(f"Получен результат {cur_element=} {parity}") 
        else:
            self.fix_queue.put(cur_element)
            print(f'Результат для {cur_element=} не верен, отправляю повторно элемент в очередь исправлений')
        

    def fix(self):
        cur_element = self.fix_queue.get()
        self.odd_or_even(cur_element)
        
    def put(self, element):
        print(f'Добавлене элемен {element=}')
        self.base.put(element)

    def get(self):
        return self.solved.get()

tasks = TaskBoard()
tasks.put(10)
tasks.put(11)
tasks.put(12)
tasks.some_work()
tasks.some_work()
tasks.some_work()
tasks.check()
while tasks.fix_queue.size():
    tasks.fix()
    tasks.check()
tasks.check()
while tasks.fix_queue.size():
    tasks.fix()
    tasks.check()
tasks.check()
while tasks.fix_queue.size():
    tasks.fix()
    tasks.check()