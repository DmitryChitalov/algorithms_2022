from memory_profiler import profile




@profile
def cell():
    class Cell:

        
        def __init__(self,integer):
            self.integer = int(integer)
        
        def __add__(self,other):
            return self.integer + other.integer

        def __sub__(self, other):
            sub = self.integer - other.integer
            return f'Клеточка стала меньше, теперь она равна: {sub} клеточкам' if sub > 0 else 'Клетка исчезла :('
        
        def __mul__(self,other):
            return(self.integer * other.integer)

        def __floordiv__(self,other):
            return(self.integer //other.integer)

        def __truediv__(self,other):
            return(self.integer /other.integer)

        def make_order(self,row):
            result = ''
            for i in range(int(self.integer / row)):
                result += '*'* row +'\n'
            result += '*'* (self.integer % row) + '\n'
            return result

    cell = Cell(999999)
    cell_2 = Cell(2)
    print(cell + cell_2)
    print(cell - cell_2)
    print(cell / cell_2)
    print(cell * cell_2)
    print(cell.make_order(6))



@profile
def cell_2():
    class Cell:

        __slots__ = ['integer','row','other']
        def __init__(self,integer):
            self.integer = int(integer)
        
        def __add__(self,other):
            return self.integer + other.integer

        def __sub__(self, other):
            sub = self.integer - other.integer
            return f'Клеточка стала меньше, теперь она равна: {sub} клеточкам' if sub > 0 else 'Клетка исчезла :('
        
        def __mul__(self,other):
            return(self.integer * other.integer)

        def __floordiv__(self,other):
            return(self.integer //other.integer)

        def __truediv__(self,other):
            return(self.integer /other.integer)

        def make_order(self,row):
            result = ''
            for i in range(int(self.integer / row)):
                result += '*'* row +'\n'
            result += '*'* (self.integer % row) + '\n'
            return result

    cell = Cell(9)
    cell_2 = Cell(2)
    print(cell + cell_2)
    print(cell - cell_2)
    print(cell / cell_2)
    print(cell * cell_2)
    print(cell.make_order(6))




if __name__ == '__main__':
    cell()
    cell_2()


#задание взято из курса основ (10урок 3 задание)
#как видно слоты очень сильно уменьшают использование памяти.