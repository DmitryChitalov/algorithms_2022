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
        self.lst = []

    def add_task(self, task):
        self.lst.insert(0, task)

    def show_task(self):
        print(self.lst)

    def erase_task(self):
        return self.lst.pop()

todo_task = Task_board()
done_task = Task_board()
redo_task = Task_board()
todo_task.add_task('lessons at 18:00')
todo_task.add_task('work at 12:00')
todo_task.add_task('phone call')


todo_task.show_task()
done_task.add_task(todo_task.erase_task())
done_task.add_task(todo_task.erase_task())
todo_task.show_task()
done_task.show_task()
redo_task.add_task(done_task.erase_task())
done_task.show_task()
redo_task.show_task()

