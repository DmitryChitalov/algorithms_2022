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
class TasksBoard:
    def __init__(self):
        self.base = []
        self.revision = []
        self.done = []

    def is_empty(self):
        return self.base == [], self.revision == [], self.done == []

    def new_task(self, item):
        self.base.insert(0, item)
    
    def to_revision(self):
        self.revision.insert(0,  self.base[-1])
        return self.base.pop()
        
    def from_base_to_done(self):
        self.done.insert(0, self.base[-1])
        return self.base.pop()
    
    def from_revision_to_done(self):
        self.done.insert(0, self.revision[-1])
        return self.revision.pop()
    
    def del_from_done(self):
        return self.done.pop()

    def size(self, queue):
        if queue == 'base':
            return len(self.base)
        elif queue == 'revision':
            return len(self.revision)
        elif queue == 'done':
            return len(self.done)
        else:
            return 'Такой очереди нет'


if __name__ == '__main__':
    qc_obj = TasksBoard()
    print(qc_obj.is_empty())  # -> True. Очереди пустые

    # помещаем объекты в очередь
    qc_obj.new_task('task1')
    qc_obj.new_task('task2')
    qc_obj.new_task('task3')
    qc_obj.new_task('task4')
    qc_obj.new_task('task5')
    qc_obj.new_task('task6')
    
    qc_obj.to_revision() #task1
    
    qc_obj.from_base_to_done() #task2
    
    qc_obj.to_revision() #task3
    
    qc_obj.from_base_to_done() #task4
    
    qc_obj.from_revision_to_done() #task1
    
    qc_obj.del_from_done() #task2
    
    print(qc_obj.base, ' кол-во задач: ', qc_obj.size('base'))
    print(qc_obj.revision, ' кол-во задач: ', qc_obj.size('revision'))
    print(qc_obj.done, ' кол-во задач: ', qc_obj.size('done'))