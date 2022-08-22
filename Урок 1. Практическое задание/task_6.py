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


class CanBan:
    def __init__(self):
        self.__basic = []
        self.__revork = []
        self.__finish = []

    def finishTransferRevork(self,indx):
        self.__revork.append(self.__finish.pop(indx))

    def basicTransferFinish(self,indx):
        self.__finish.append(self.__basic.pop(indx))

    def revokTransferToFinish(self,indx):
        self.__finish.append(self.__revork.pop(indx))

    def addTaskToBasic(self,nunber):
        self.__basic.append(nunber)

    def printBasic(self):
        print(self.__basic)

    def printRevork(self):
        print(self.__revork)

    def printFinish(self):
        print(self.__finish)
    

canban = CanBan()
print("Добавляем задачи в ветку с заданиями")
canban.addTaskToBasic(123)
canban.addTaskToBasic(23)
canban.addTaskToBasic(342)
canban.addTaskToBasic(8)
print("Печать доски заданий")
canban.printBasic()
print("Переносим задачу в решенные")
canban.basicTransferFinish(2)
canban.basicTransferFinish(0)
print("Печать выполненых задач")
canban.printFinish()
print("Перенос задач в очередь на дороботку")
canban.finishTransferRevork(1)
canban.finishTransferRevork(0)
canban.printRevork()
print("Перенос задачи в выполенные")
canban.revokTransferToFinish(0)
print("Печать заданий на дороботку")
canban.printRevork()
print("Печать выполненых заданий")
canban.printFinish()
print("Печать оставшихся задач")
canban.printBasic()