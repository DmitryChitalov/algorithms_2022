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
    """
    Доска Задач
    """
    def __init__(self):
        self.base = []
        self.modification = []
        self.solved = []

    def is_empty(self):
        """ Пустой список задач"""
        return not self.base

    def new_task(self, task):
        """Новая задача"""
        self.base.insert(0, task)

    def to_modification(self):
        """Список на дорабортку"""
        self.modification.insert(0, self.base.pop())

    def to_solved(self, board_from):
        """Список решенных задач"""
        self.solved.insert(0, board_from.pop())

    def size(self):
        """ Размер списка"""
        return len(self.base)


if __name__ == "__main__":
    tb_obj = TaskBoard()
    tb_obj.new_task('Приготовить завтрак')
    tb_obj.new_task("Помыть посуду")
    tb_obj.new_task("Убраться в доме")
    tb_obj.new_task("Переодеться")
    tb_obj.new_task("Выйти из дома")
    tb_obj.new_task("Поехать на море")
    print(tb_obj.base)
    print(tb_obj.modification, tb_obj.solved)
    print()
    tb_obj.to_solved(tb_obj.base)
    tb_obj.to_modification()
    tb_obj.to_modification()
    print(tb_obj.base)
    print(tb_obj.modification)
    print(tb_obj.solved)
    print()
    tb_obj.to_solved(tb_obj.modification)
    print(tb_obj.base)
    print(tb_obj.modification)
    print(tb_obj.solved)
    print(tb_obj.size())
