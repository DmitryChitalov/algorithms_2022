"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""
class PlatesPack:
    def __init__(self, limit):
        self.plates = []
        self.limit = limit
          
    def add(self, pl):
        if len(self.plates[len(self.plates) - 1]) < self.limit:
            self.plates[len(self.plates) - 1].append(pl)
        else:
            self.plates.append([])
            self.plates[len(self.plates) - 1].append(pl) 
    
    def delete (self)
        result = self.plates[len(self.plates) - 1].pop()
        if len(self.plates[len(self.plates) - 1]) == 0:
            self.plates.pop()
        return result
    
if __name__ == '__main__':
    plate = PlatesPack(3)
    plate.add('one')
    plate.add('two')
    plate.add('three')
    plate.add('four')
    plate.add('five')
    print(plate)
    print(plate.delete())
