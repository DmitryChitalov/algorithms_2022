"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
!!!!!!!!!
В моем понимание на доработку можно отправить только решеную задачу,
т.е. из первой очереди задача может отправиться только в третью(решеную),
только потом может попасть в очередь на доработку. Исходя из этого мое решение
!!!!!!!!
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

class QueueClass:
    def __init__(self):
        self.elems = []
        self.rework = []
        self.resolved = []

    def to_queue_base(self, item):
        self.elems.insert(0, item)

    def from_queue_base_resolved(self):
        return self.resolved.append(self.elems.pop())

    def from_queue_resolved_rework(self):
        return self.rework.append(self.resolved.pop())

    def from_queue_rework_resolved(self):
        return self.resolved.append(self.rework.pop())

    def size(self):
        return f'Базовая очередь: {len(self.elems)} \n' \
               f'Очередь на доработку: {len(self.rework)} \n' \
               f'Решеные задачи: {len(self.resolved)} '

    def __str__(self):
        return f'Базовая очередь: {self.elems} \n' \
               f'Очередь на доработку: {self.rework} \n' \
               f'Решеные задачи: {self.resolved} '


if __name__ == '__main__':
    qc_obj = QueueClass()


    # помещаем объекты в очередь
    qc_obj.to_queue_base('1. Создание БД')
    qc_obj.to_queue_base('2. Анализ предметной области')
    qc_obj.to_queue_base('3. Нормализация отношений в инфо модели')
    qc_obj.to_queue_base('4. Создание структуры данных')
    qc_obj.to_queue_base('5. Разработка интерфейса')
    qc_obj.to_queue_base('6. Разработка доп модулей')
    qc_obj.to_queue_base('7. Тестирование и отладка инфо системы')
    qc_obj.to_queue_base('8. Внедрение')
    qc_obj.to_queue_base('9. Эксплуатация')

    qc_obj.from_queue_base_resolved()
    qc_obj.from_queue_base_resolved()
    qc_obj.from_queue_base_resolved()
    qc_obj.from_queue_base_resolved()
    qc_obj.from_queue_base_resolved()
    qc_obj.from_queue_resolved_rework()
    qc_obj.from_queue_resolved_rework()
    qc_obj.from_queue_resolved_rework()
    qc_obj.from_queue_rework_resolved()

    print(qc_obj.size())
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(qc_obj)

"""
В моем понимание на доработку можно отправить только решеную задачу,
т.е. из первой очереди задача может отправиться только в третью(решеную),
только потом может попасть в очередь на доработку. Исходя из этого мое решение
"""