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

from task_6_class import DeskClass


def solving(task_lst):
    desk_obj = DeskClass()

    for task in task_lst:
        desk_obj.to_task(task)
    print(desk_obj.task)

    while desk_obj.size() > 0:
        desk_obj.to_correct(desk_obj.from_task())
        desk_obj.to_solved(desk_obj.from_task())
    print(desk_obj.correct)
    print(desk_obj.solved)

    while desk_obj.size_correct() > 0:
        desk_obj.to_solved(desk_obj.from_correct())
    print(desk_obj.solved)

    return desk_obj.from_solved()


print(solving(["Задача 1", "Задача 2", "Задача 3", "Задача 4", "Задача 5", "Задача 6"]))

