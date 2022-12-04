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

class Task_board:
    def __init__(self):
        self.basic = []
        self.modification = []
        self.solved = []

    def adding_a_task(self, task):
        if task not in self.basic and task not in self.modification:
            self.basic.append(task)
        else:
            print('Данная задача уже имеется и находится в процессе решения')


    def moving_to_revision(self, task):
        if task in self.basic:
            self.basic.remove(task)
            self.modification.append(task)
        else:
            print('Данная задача отсутствует в списке базовых задач.')

    def move_to_resolved(self, task):
        if task in self.basic:
            self.basic.remove(task)
            self.solved.append(task)
        elif task in self.modification:
            self.modification.remove(task)
            self.solved.append(task)
        else:
            print('Данная задача отсутствует в списках задач.')

    def view_all_tasks(self):
        print(f'Базовые задачи {self.basic}\nЗадачи на доработке {self.modification}\nРешенные задачи {self.solved}')



building_a_house = Task_board()
building_a_house.adding_a_task('Написание проекта')
building_a_house.move_to_resolved('Написание проекта')
building_a_house.adding_a_task('Покупка стройматериалов')
building_a_house.adding_a_task('Подбор строительной команды')
building_a_house.moving_to_revision('Покупка стройматериалов')
building_a_house.adding_a_task('Подбор строительной команды')
building_a_house.adding_a_task('Стройка фундамента')
building_a_house.move_to_resolved('Подбор строительной команды')
building_a_house.adding_a_task('Стройка коробки дома')
building_a_house.view_all_tasks()
