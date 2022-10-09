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
        self.elems = {
            'base_tasks': [],
            'solved_tasks': [],
            'revising_tasks': []
        }

    def show_unsolved(self):
        print('Открытые задачи:')
        for i in range(len(self.elems['base_tasks'])):
            print(f"{i+1}. {self.elems['base_tasks'][i]}")
        if len(self.elems['revising_tasks']) > 0:
            print('Задачи на доработке:')
            for i in range(len(self.elems['revising_tasks'])):
                print(f"{i+1}. {self.elems['revising_tasks'][i]}")
        else:
            print('Задач на доработку нет')

    def show_solved(self):

        if len(self.elems['solved_tasks']) > 0:
            print('Выполненные задания:')
            for i in range(len(self.elems['solved_tasks'])):
                print(f"{i+1}. {self.elems['solved_tasks'][i]}")
        else:
            print('Еще ни одна задача не выполнена!!!')

    def add_task(self, task):
        self.elems['base_tasks'].append(task)

    def solve_task(self):
        self.elems['solved_tasks'].append(self.elems['base_tasks'].pop(0))

    def revise_task(self):
        self.elems['revising_tasks'].append(self.elems['base_tasks'].pop(0))

    def delete_task(self, from_board):
        try:
            return self.elems[from_board].pop(0)
        except:
            print('введено неверное значение аргумента')

    def check_revision(self, check=True):
        if check:
            self.elems['solved_tasks'].append(self.elems['revising_tasks'].pop(0))
        else:
            self.elems['base_tasks'].append(self.elems['revising_tasks'].pop(0))


if __name__ == '__main__':
    tasks = TasksBoard()
    tasks.add_task('Написать письмо')
    tasks.add_task('Составить анализ предложений')
    tasks.add_task('Составить план мероприятий')
    tasks.add_task('Составить отчет по стали за 3 квартал')
    tasks.add_task('Провести тендер')
    tasks.add_task('Написать приложение по рассмотрению идей сотрудников')
    tasks.add_task('Провести тестирование первой партии сырья')
    tasks.add_task('Согласовать договор по поставке комплектующих')
    tasks.add_task('Провести бенчмаркинг по гальванопокрытию')
    tasks.show_unsolved()
    tasks.show_solved()
    tasks.solve_task()
    tasks.show_solved()
    tasks.show_unsolved()
    tasks.revise_task()
    tasks.revise_task()
    tasks.revise_task()
    tasks.show_unsolved()
    tasks.check_revision()
    tasks.check_revision(False)
    tasks.show_unsolved()
    tasks.show_solved()
    tasks.delete_task('base_tasks')
    tasks.show_unsolved()