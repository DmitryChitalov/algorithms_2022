from random import randint

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

from random import randint

class StackClass:
  def __init__(self):
    self.elems = list()
  
  def push_in(self, el):
    self.elems.append(el)
  
  def stack_size(self):
    return len(self.elems)
  
  def clear_stack(self):
    self.elems = list() 
 

if __name__ == '__main__':
  
  stacks = list()
  stack = StackClass()
  
  amount_of_dishes = randint(0, 100)
  max_size = randint(0,10)
  
  for i in range(1, amount_of_dishes + 1):
    now_size = stack.stack_size()
    if now_size < max_size:
      stack.push_in(f'dish_{i}')
    else:
      stacks.append(stack.elems)
      stack.clear_stack()
      stack.push_in(f'dish_{i}')

  stacks.append(stack.elems)
  print(amount_of_dishes, max_size)
  print(stacks)
      
 
  
  
  
