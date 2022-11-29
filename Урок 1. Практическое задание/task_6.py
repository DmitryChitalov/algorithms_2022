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
class TasksDesk:
    def __init__(self):
        self.lst = []

    def plus_task(self, task):
        self.lst.insert(0, task)

    def show_tasks(self):
        print(self.lst)

    def minus_task(self):
        return self.lst.pop()


todo_tasks = TasksDesk()
done_tasks = TasksDesk()
redo_tasks = TasksDesk()

todo_tasks.plus_task('wash_dishes')
todo_tasks.plus_task('find_job')
todo_tasks.plus_task('find_meaning_of_life')
todo_tasks.plus_task('make_more_lists')

todo_tasks.show_tasks()

done_tasks.plus_task(todo_tasks.minus_task())
done_tasks.plus_task(todo_tasks.minus_task())

todo_tasks.show_tasks()
done_tasks.show_tasks()

redo_tasks.plus_task(done_tasks.minus_task())

done_tasks.show_tasks()
redo_tasks.show_tasks()