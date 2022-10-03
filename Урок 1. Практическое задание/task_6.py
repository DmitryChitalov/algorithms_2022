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

def show_tasks():
    print(basic_tasks.tasks)
    print(fix_tasks.tasks)
    print(resolved_tasks.tasks)
    print('---')

class TaskBoard():
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

    def move_task(self, lst):
        if not self.tasks:
            print('В этом списке нет задач')
        else:
            lst.add_task(self.tasks[-1])
            self.tasks.pop()

basic_tasks = TaskBoard()
fix_tasks = TaskBoard()
resolved_tasks = TaskBoard()

basic_tasks.add_task('Задача 1')
basic_tasks.add_task('Задача 2')
show_tasks()

basic_tasks.move_task(fix_tasks)
show_tasks()

fix_tasks.move_task(resolved_tasks)
show_tasks()

resolved_tasks.move_task(basic_tasks)
show_tasks()

basic_tasks.move_task(fix_tasks)
fix_tasks.move_task(resolved_tasks)
show_tasks()