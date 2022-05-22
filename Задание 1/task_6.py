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
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)

class TasksClass:
    def __init__(self, list_queue_name):
        self.list_queue_name = list_queue_name
        self.dict_queue = {}
        for self.queue_name in self.list_queue_name:
            self.dict_queue[self.queue_name] = QueueClass()
        
    def get_queue(self, name):
        if name in self.list_queue_name:
            return self.dict_queue[name]
        else:
            return None

    def to_queue(self, name, item):
        if self.get_queue(name) != None:
            self.get_queue(name).to_queue(item)
        
    def from_to(self, from_name, to_name):
        if self.get_queue(from_name) == None:
            return from_name + ' нет'
        if self.get_queue(from_name).is_empty():
            return 'from ' + from_name + ' не выполнено, очередь пустая'
        if self.get_queue(to_name) == None:
            return to_name + ' нет'
        self.to_queue(to_name, self.get_queue(from_name).from_queue())
        return 'from ' + from_name + ' to ' + to_name + ' выполнено'
    
Tasks = TasksClass(['Base', 'Work', 'Done'])
Tasks.to_queue('Base', 'task1')
Tasks.to_queue('Base', 'task2')
Tasks.to_queue('Base', 'task3')
Tasks.to_queue('Base', 'task4') # Base: 1, 2, 3, 4
Tasks.from_to('Base', 'Work')
Tasks.from_to('Base', 'Work') # Base: 3, 4; Work: 1, 2
Tasks.from_to('Base', 'Done') # Base: 4; Work: 1, 2; Done: 3
Tasks.from_to('Work', 'Done') # Base: 4; Work: 2; Done: 3, 1
print('В Base ' + Tasks.get_queue('Base').from_queue())
print('В Work ' + Tasks.get_queue('Work').from_queue())
print('В Done ' + Tasks.get_queue('Done').from_queue())
print('В Done ' + Tasks.get_queue('Done').from_queue())
