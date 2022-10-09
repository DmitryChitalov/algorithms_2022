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
#  Задание не понятное.
#  Как нерешенные задачи могут отправляться на доработку?
#  Как понять, из какой из двух очередей брать текущую задачу?
#  Реализовал очередь задач разработчика и проверяющего (разработкчик отправляет на проверку,
# а по результатам проверки задача либо закрывается, либо возвращается в очередь разработчика)


class Queue:
    def __init__(self):
        self.contents = []

    def __str__(self):
        return str(self.contents)

    def push(self, item):
        self.contents.insert(0, item)

    def pop(self):
        return self.contents.pop()


class TaskBoard:
    def __init__(self):
        self.opened_tasks = Queue()
        self.review_tasks = Queue()
        self.closed_tasks = []

    def __str__(self):
        return str(self.opened_tasks) + '/' + str(self.review_tasks)

    def add_task(self, item):
        self.opened_tasks.push(item)

    def send_task_to_review(self):
        task = self.opened_tasks.pop()
        self.review_tasks.push(task)

    def close_task(self):
        task = self.review_tasks.pop()
        self.closed_tasks.append(task)

    def return_task_from_review(self):
        task = self.review_tasks.pop()
        self.opened_tasks.push(task)

    def get_current_task(self):
        if len(self.opened_tasks.contents) > 0:
            return self.opened_tasks.contents[len(self.opened_tasks.contents) - 1]
        else:
            return None

    def get_current_task_in_review(self):
        if len(self.review_tasks.contents) > 0:
            return self.review_tasks.contents[len(self.review_tasks.contents) - 1]
        else:
            return None

    def get_closed_tasks(self):
        return self.closed_tasks


if __name__ == '__main__':
    task_board = TaskBoard()
    for i in range(10):
        task_board.add_task('Задача ' + str(i))
    print(task_board)
    print(f'Текущая задача/доработка: {task_board.get_current_task()}/'
          f'{task_board.get_current_task_in_review()}')
    task_board.send_task_to_review()
    print(f'На проверку. Текущая задача/доработка: {task_board.get_current_task()}/'
          f'{task_board.get_current_task_in_review()}')
    print(task_board)
    task_board.return_task_from_review()
    print(f'На доработку. Текущая задача/доработка: {task_board.get_current_task()}/'
          f'{task_board.get_current_task_in_review()}')
    print(task_board)
    task_board.send_task_to_review()
    print(f'На проверку. Текущая задача/доработка: {task_board.get_current_task()}/'
          f'{task_board.get_current_task_in_review()}')
    print(task_board)
    task_board.close_task()
    print(f'Закрыто. Текущая задача/доработка: {task_board.get_current_task()}/'
          f'{task_board.get_current_task_in_review()}')
    print(task_board)
    print(task_board.get_closed_tasks())
