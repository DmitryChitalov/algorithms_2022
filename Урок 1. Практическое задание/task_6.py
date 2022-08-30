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


class TaskBoard:
    def __init__(self):
        self.basic_tsk = []
        self.correction_tsk = []
        self.solved_tsk = []
        self.ord = 0

    def add_task(self, condition):
        self.basic_tsk.append(condition)
        self.ord += 1
        return self.basic_tsk

    def base_tasks(self):
        ask = input('Задача 0 решена?(yes, no)')
        if ask == 'yes':
            tsk = self.basic_tsk.pop(0)
            self.solved_tsk.append(tsk)
            return f'Basic: {self.basic_tsk}, Correction: {self.correction_tsk}, Solved: {self.solved_tsk}'
        elif ask == 'no':
            tsk_2 = self.basic_tsk.pop(0)
            self.correction_tsk.append(tsk_2)
            return f'Basic: {self.basic_tsk}, Correction: {self.correction_tsk}, Solved: {self.solved_tsk}'
        else:
            return 'Нет такого варианта ответа(yes или no)'

    def correction_tasks(self):
        quest = input(f'Задача 0 решена?(yes, no)')
        try:
            if quest == 'yes':
                task = self.correction_tsk.pop(0)
                self.solved_tsk.append(task)
                return f'Basic: {self.basic_tsk}, Correction: {self.correction_tsk}, Solved: {self.solved_tsk}'
            elif quest == 'no':
                return 'Корректируйте задачу дальше.'
            else:
                return 'Нет такого варианта ответа!(yes или no)'
        except IndexError:
            return 'Список задач на корректировку пуст'

    def del_tasks(self, group_of_tsks, index_of_tsk): # в аргументы передаем группу в которой наше задание(basic, correction, solved) и индекс задачи
        if group_of_tsks == 'basic':
            self.basic_tsk.pop(index_of_tsk)
            return f'Basic: {self.basic_tsk}, Correction: {self.correction_tsk}, Solved: {self.solved_tsk}'
        elif group_of_tsks == 'correction':
            self.correction_tsk.pop(index_of_tsk)
            return f'Basic: {self.basic_tsk}, Correction: {self.correction_tsk}, Solved: {self.solved_tsk}'
        elif group_of_tsks == 'solved':
            self.solved_tsk.pop(index_of_tsk)
            return f'Basic: {self.basic_tsk}, Correction: {self.correction_tsk}, Solved: {self.solved_tsk}'


tb = TaskBoard()
tb.add_task('Сходить в душ')
tb.add_task('Сходить в магазин')
tb.add_task('Погулять с собакой')
tb.add_task('Работа с 10-18')
tb.add_task('Ужин с семьей')
print(tb.basic_tsk)
print(tb.base_tasks())
print(tb.correction_tasks())
print(tb.del_tasks('basic', 1))
# если задача решена то добавить в решенные, если не решена то отправить на корректировку
# то ест нужно создать метод который будет спрашивать решена ли задача. И если решена то добавлять в решенные и удалять из
# базовых. если нужна корректировка, то добавлять в список и когда задача доработана удлять из базового и добавлять в решенные.