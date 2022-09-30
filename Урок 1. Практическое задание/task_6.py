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

from random import choice


class Tasks:
    def __init__(self):
        self.new = []
        self.to_edit = []
        self.completed = []
        self.next_work_switch = 0


    def is_empty(self, type):
        if type == 'new':
            return  not bool(self.new)
        if type == 'to_edit':
            return not bool(self.to_edit)
        if type == 'completed':
            return not bool(self.completed)
        raise ValueError("incorrect TYPE")


    def push_to_new(self,el):
        self.new.append(el)
        print(f' work {el} append to new ')

    def work(self):
        self.next_work_switch_turn()
        # print(f'switch = {self.next_work_switch}')
        if self.next_work_switch:
            if self.new :
                el = self.new.pop(0)
                print(f' from new {el} work in progress , move to completed')
                self.completed.append(el)
                return
            elif self.to_edit:
                el = self.to_edit.pop(0)
                print(f' new is empty;  from edit {el} work in progress , move to completed')
                self.completed.append(el)
                return
            else:
                print (f' work stand-by : Stack New is empty , stack to_edit is empty' )
                return
        else:
            if self.to_edit:
                el = self.to_edit.pop(0)
                print(f' from edit {el} work in progress , move to completed')
                self.completed.append(el)
                return
            elif self.new:
                el = self.new.pop(0)
                print(f' edit is empty,  from new  {el} work in progress , move to completed')
                self.completed.append(el)
                return
            else:
                print(f' work stand-by : Stack New is empty , stack to_edit is empty')
                return

    def check(self):
        if self.completed != []:
            el = self.completed.pop(0)
            print(f'checking work {el}')
            action = choice([1, 2, 3])
            if action == 1 or action == 2:
                print(f'work {el} completed and closed')
                return
            else:
                print(f' work {el} returned to edit ')
                self.to_edit.append(el)
                return
        else :
            print(f' check stand-by : Stack completed is empty ')
            return


    def info(self):
        print(f' new = {self.new}')
        print(f' to_edit = {self.to_edit}')
        print(f' completed = {self.completed}')

    def next_work_switch_turn(self):
        if self.next_work_switch == 0:
            self.next_work_switch = 1
        else:
            self.next_work_switch = 0


if __name__ == '__main__':

    project = Tasks()
    project.info()
    print(f'project.new.is_empty : {project.is_empty("new")}')
    print(f'project.to edit.is_empty : {project.is_empty("to_edit")}')
    print(f'project.to edit.is_empty : {project.is_empty("completed")}')

    for n in range (0,10):
        task_name = 't'+str(n)
        project.push_to_new(task_name)
        project.info()

    for n in range (11, 20):
        print('---------------------------------')
        task_name = 't' + str(n)
        project.push_to_new(task_name)
        project.work()
        project.work()
        project.info()
        project.check()
        project.check()
        project.info()

    for n in range (21, 40):
        print('---------------------------------')
        project.work()
        project.work()
        project.info()
        project.check()
        project.check()
        project.info()
        if project.is_empty("new") and \
            project.is_empty("to_edit") and \
            project.is_empty("completed"):
            break


