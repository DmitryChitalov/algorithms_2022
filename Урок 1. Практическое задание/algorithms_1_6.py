"""
Задание 6. На закрепление навыков работы со временем
Примечание: в этом задании сообщайте о своих знаниях по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "Доска задач".
Структура должна предусматривать наличие несольких очередных задач, например
1) откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
решения по корректировке
3) список решенных задач, куда задачи перемещаются из региональных цепочек или
очереди на доработку
После реализации структуры проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class Tasks:
    """Создаем класс Задачи
    task - сама задача (текст)
    solved - критерий сделанности задачи"""
    def __init__(self, task: str):
        self.solved = 0
        self.task = task

    def __str__(self):
        return self.task


waiting_line = []
make_line = []
made_line = []

task1 = Tasks('Добавить фичу')
task2 = Tasks('Пофиксить баг')
task3 = Tasks('Оптимизировать код')

waiting_line.append(task1)
waiting_line.append(task2)
waiting_line.append(task3)


print('', 'До перевода в работу ожидают: ', *waiting_line, sep='\n')
make_line.append(waiting_line.pop(0))
# print('После первого перевода в работу ожидают: ', waiting_line)
# print('В работе: ', make_line)
make_line.append(waiting_line.pop(0))
print('', 'После второго перевода в работу ожидают: ', *waiting_line, sep='\n')
print('', 'В работе: ', *make_line, sep='\n')

make_line[0].solved = 1  # Переводим задачу в "готовые"

for task in make_line:
    if task.solved:
        made_line.append(task)
    else:
        waiting_line.append(task)

make_line.clear()

print('', 'После проверки таски распределены так: ', sep='\n')
print('', 'В ожидании: ', *waiting_line, sep='\n')
print('', 'Готовые: ', *made_line, sep='\n')
print('', 'В работе: ', *make_line, sep='\n')

