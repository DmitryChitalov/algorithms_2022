"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskBoard:
    def __init__(self):
        self.to_do = []
        self.in_progress = []
        self.completed = []

    def is_empty(self):
        return self.to_do == [] and self.in_progress == [] and self.completed == []

    def to_list(self, list_to, task):
        if list_to.lower() == 'to_do':
            self.to_do.insert(0, task)
        elif list_to.lower() == 'in_progress':
            self.in_progress.insert(0, task)
        else:
            self.completed.insert(0, task)

    def from_list_to_list(self, list_from, list_to):
        if list_from.lower() == 'to_do':
            task_to_transfer = self.to_do.pop()
        elif list_to.lower() == 'in_progress':
            task_to_transfer = self.in_progress.pop()
        else:
            task_to_transfer = self.completed.pop()

        self.to_list(task_to_transfer, list_to)

    def size(self):
        return len(self.to_do), len(self.in_progress), len(self.completed)


if __name__ == '__main__':
    t_b_1 = TaskBoard()

    while True:
        user_choice = input('Choose the action: 1 - add new task/ 2 - transfer a task from one list to another/'
                            '3 - check if all the lists are empty/ 4 - check the size of lists/ 5 - quit. '
                            '\nEnter the number: ')
        if user_choice == '1':
            t_b_1.to_list(input('What list do you want to edit (to_do/in_progress/completed)? '),
                          input('Enter the task: '))
        elif user_choice == '2':
            t_b_1.from_list_to_list(input('What list do you want to transfer task from (to_do/in_progress/completed)? '),
                                    input('What list do you want to transfer task to (to_do/in_progress/completed)? '))
        elif user_choice == '3':
            print(t_b_1.is_empty())
        elif user_choice == '4':
            print(t_b_1.size())
        else:
            break
