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

class General:
    def __init__(self):
        self.elems = []
        
    def add(self, item):
        self.elems.insert(0, item)
        
    def remove(self):
        return self.elems.pop()
      
          
class TaskBoard:
    def __init__(self):
    # Основная очередь.
        self.base = General()
    # Очередь доработки.
        self.rework = General()
    # Решенные задачи.
        self.solved = []
        
    def close_task(self):
    # Закрываем основную задачу и помещаем в решенные
        task = self.base.remove()
        self.solved.append(task)
        
    def to_current(self, item):
    # Добавляем задачи в текущие
        self.base.add(item)
        
    def to_rework(self):
    # Переносим задачу на доработку.
        task = self.base.remove() 
        self.rework.add(task)
        
    def to_base(self):
    # Возвращаем из доработки в основную очередь
        task = self.rework.remove()
        self.base.add(task)
       
if __name__ == '__main__':
    task_board = TaskBoard()
    task_board.to_current('Task_One')
    task_board.to_current('Task_Two')
    task_board.to_current('Task_Thee')
    task_board.to_current('Task_Four')
    task_board.to_current('Five')
    task_board.close_task()
    task_board.to_rework()
    task_board.to_base()
