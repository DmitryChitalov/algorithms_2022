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

"""
Что нужно включить в класс:
    1. инициализация: создание списков задач (текущие, решённые, корректируемые, удалённые)
    2. str - чтобы смотреть на доску задач
    3. replace_to_current - переместить задачу в текущий список
        нельзя переместить решённую задачу
        если задача была удалена, она удаляется из списка удалённых и добавляется в текущий
    4. функция replace_to_correct - переместить задачу в очередь на корректировку решения
        можно переместить только задачу из решённого списка
    5. функция replace_to_solve - переместить задачу в очередь решённых
        можно переместить задачу только из текущего списка или из корректировки, 
            в соответствующем списке задача удаляется
    6. функция delete - удалить последнюю задачу из текущего списка
        проверка на наличие задач
    7. функция basket - список удалённых задач
    8. функция check - проверка статуса задачи
    9. функция count - подсчёт задач в каждой очереди
    10. функция total_delete - удаляем все текущие задачи
"""


class TaskBoard:
    def __init__(self):
        self.current_tasks = []
        self.correct_tasks = []
        self.solve_tasks = []
        self.delete_tasks = []

    def __str__(self):
        task_dict = {'current_tasks': self.current_tasks,
                     'correct_tasks': self.correct_tasks,
                     'solve_tasks': self.solve_tasks
                     }
        return str(task_dict)

    def replace_to_current(self, task):
        if task in self.solve_tasks:
            return 'Задача уже решена'
        elif task in self.delete_tasks:
            self.delete_tasks.remove(task)
            self.current_tasks.append(task)
            return 'Задача {} добавлена в текущие'.format(task)
        else:
            self.current_tasks.append(task)
            return 'Задача {} добавлена в текущие'.format(task)

    def replace_to_correct(self, task):
        if task in self.solve_tasks:
            self.solve_tasks.remove(task)
            self.correct_tasks.append(task)
            return 'Решение задачи {} отправлено на корректировку'.format(task)
        else:
            return 'Корректировать можно только решённую задачу'

    def replace_to_solve(self, task):
        if task in self.correct_tasks:
            self.solve_tasks.append(task)
            self.correct_tasks.remove(task)
            return 'Задача {} решена'.format(task)
        elif task in self.current_tasks:
            self.solve_tasks.append(task)
            self.current_tasks.remove(task)
            return 'Задача {} решена'.format(task)
        elif task in self.delete_tasks:
            return 'Задача {} была удалена'.format(task)
        elif task in self.solve_tasks:
            return 'Задача {} уже в списке решённых'.format(task)
        else:
            return 'В решённые можно поместить только задачи из текущего списка или из корректировки'

    def delete(self):
        if len(self.current_tasks) != 0:
            new_current_tasks = self.current_tasks.pop()
            self.delete_tasks.append(new_current_tasks)
            return 'Последняя текущая задача удалена'

        else:
            return 'Нет текущих задач!'

    def basket(self):
        if len(self.delete_tasks) != 0:
            return self.delete_tasks
        else:
            return 'Нет удалённых задач'

    def check(self, task):
        if task in self.current_tasks:
            return 'Задача {} в текущем списке'.format(task)
        elif task in self.solve_tasks:
            return 'Задача была решена'.format(task)
        elif task in self.correct_tasks:
            return 'Задача на корректировке'.format(task)
        elif task in self.delete_tasks:
            return 'Задача была удалена'.format(task)
        else:
            return 'Нет такой задачи'

    def count(self):
        task_dict = {'current_tasks': len(self.current_tasks),
                     'correct_tasks': len(self.correct_tasks),
                     'solve_tasks': len(self.solve_tasks)
                     }
        return task_dict

    def total_delete(self):
        for task in self.current_tasks:
            self.delete_tasks.append(task)
        self.current_tasks.clear()
        return 'Все текущие задачи удалены'
        # return self.current_tasks


task_board = TaskBoard()
print(task_board) # посмотрим на пустую доску
print(task_board.replace_to_solve('task1')) # попробуем поместить задачу в решённые
print(task_board.replace_to_correct('task1')) # попробуем поместить задачу в корректируемые
print(task_board.replace_to_current('task1')) # накидаем задач в текущий список
print(task_board.replace_to_current('task2'))
print(task_board.replace_to_current('task3'))
print(task_board.replace_to_current('task4'))
print(task_board.replace_to_solve('task3')) # поместим задачу 3 в решённые
print(task_board.replace_to_solve('task2')) # поместим задачу 2 в решённые
print(task_board.replace_to_solve('task3')) # попробуем ещё раз решить задачу 3
print(task_board.replace_to_correct('task2')) # отправим на корректировку решения задачу 2
print(task_board) # посмотрим на доску
print(task_board.check('task1')) # проверим статус задачи 1
print(task_board.count()) # посчитаем задачи во всех списках
print(task_board.delete()) # удалим последнюю задачу из текущего, это задача 4
print(task_board) # проверим доску, что задачи 4 нет в текущих
print(task_board.basket()) # проверим корзину на наличие задачи 4
print(task_board.replace_to_current('task4')) # вернём задачу 4 в список текущих задач
print(task_board) # проверим доску задач
print(task_board.basket()) # проверим, что корзина пуста
print(task_board.total_delete()) # удалим все текущие задачи
print(task_board.basket()) # посмотрим в корзину
print(task_board) #  проверим задачи на доске

