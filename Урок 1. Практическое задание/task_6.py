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

class Task:
    task_base = []
    task_done=[]
    task_redo = []

    def __init__(self,task_description):
        self.task_description = task_description
        self.task_base.append(self.task_description)

    def view_task(self):
        return print(self.task_description)

    def view_all_tasks(self):
        return print(f'Очередь текущих задач: {self.task_base} \nОчередь выполненных задач: {self.task_done} \n'
                     f'Очередь задач на доработке:{self.task_redo}' )

    def done_task(self):
        for task in self.task_base:
            if self.task_description == task:
                self.task_done.append(self.task_description )
                self.task_base.remove(self.task_description)
        for task in self.task_redo:
            if self.task_description == task:
                self.task_done.append(self.task_description )
                self.task_redo.remove(self.task_description)
        return print('Задача выполнена: ',self.task_description)


    def redo_task(self):
        for task in self.task_base:
            if self.task_description == task:
                self.task_redo.append(self.task_description)
                self.task_base.remove(self.task_description)
        return print('Задача на доработке: ', self.task_description)




a=Task('Задача А')
b=Task('Задача B')
c = Task('Задача С')
d= Task('Задача D')


a.view_task()
b.view_task()
c.view_task()
d.view_task()
a.done_task()
d.redo_task()
a.view_all_tasks()


