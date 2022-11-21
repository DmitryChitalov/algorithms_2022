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
import random


# Реализуем структуру "Стопка тарелок", представляющую собой стек
class PlatesStack:
    def __init__(self):
        self.max_size = random.randint(5, 10)
        self.plates = []

    def is_empty(self):
        return self.plates == []

    def stack_size(self):
        return len(self.plates)

    # Основное добавление тарелок будет реализовано "через шкаф"
    # Поэтому в этом методе просто не дадим переполнить стопку
    def push_in(self, plate):
        if self.stack_size() < self.max_size:
            self.plates.append(plate)
        else:
            print('Стопка заполнена!')

    def pop_out(self):
        return self.plates.pop()

    def get_val(self):
        return self.plates[len(self.plates) - 1]


# Реализуем структуру "Полка со стопками", представляющую собой несколько "Стопок тарелок":
class PlatesStacksShelf:
    # У шкафа также будет случайно определяться кол-во помещающихся в него стопок
    def __init__(self, stack_of_plates):
        self.max_size = random.randint(2, 5)
        self.stacks = [stack_of_plates]  # Изначально сделаем 1 место для стопки в шкафу

    def is_empty(self):
        return self.stacks == []

    def stack_size(self):
        return len(self.stacks)

    # Добавлять тарелку можно будет по принципу LIFO
    # Если уже существующая стопка тарелок достигает макс. размера, создается новая стопка
    # (новый экземпляр класса PlatesStack) и тарелка добавляется в него
    def push_in(self, existing_plates_stack, plate_num):
        for _ in range(plate_num):
            if self.stack_size() <= self.max_size:
                if existing_plates_stack.stack_size() < existing_plates_stack.max_size:
                    existing_plates_stack.push_in('plate')
                elif existing_plates_stack.stack_size() == existing_plates_stack.max_size and \
                        self.stack_size() != self.max_size:
                    existing_plates_stack = PlatesStack()
                    self.stacks.append(existing_plates_stack)
                    existing_plates_stack.push_in('plate')
            else:
                print('Шкаф заполнен!')
                break

    def pop_out(self):
        return self.stacks.pop()

    def get_val(self):
        return self.stacks[len(self.stacks) - 1]


# Создадим первую стопку:
first_stack = PlatesStack()
# Посмотрим её вместительность:
print(f'Вместимость первой стопки тарелок: {first_stack.max_size} шт.')
print()

# Поместим эту стопку в шкаф:
new_shelf = PlatesStacksShelf(first_stack)
# Посмотрим его вместительность:
print(f'Вместимость шкафа: {new_shelf.max_size} стопок')
print()

# Будем добавлять в первую стопку тарелки "через шкаф" так, чтобы создавалась новая стопка:
new_shelf.push_in(first_stack, 21)
print(f'Кол-во стопок в шкафу: {new_shelf.stack_size()} шт.')
for i in range(len(new_shelf.stacks)):
    print(f'Вместимость {i + 1}-й стопки: {new_shelf.stacks[i].max_size} шт.')
    print(f'Кол-во тарелок в {i + 1}-й стопке: {new_shelf.stacks[i].stack_size()} шт.')
    print()
print()

# При этом можно вытащить из первой стопки тарелку через метод "стопки"
# и это будет та же самая топка, что находится в шкафу.
# Попробуем с первой стопкой:
first_stack.pop_out()
print(f'Кол-во тарелок в первой стопке после изъятия 1 тарелки: {first_stack.stack_size()} шт.')
# Проверим одинаковое кол-во, обратившись к этой стопке через шкаф:
print(f'Кол-во тарелок в первой стопке после изъятия 1 тарелки: {new_shelf.stacks[0].stack_size()} шт.')
print()

# Шкаф также подчиняется принципу LIFO, т.е. вытащить можно только последнюю стопку:
pulled_stack = new_shelf.pop_out()
# Можно удостовериться, что у этой стопки аналогичные характеристики, что были у последней стопки в шкафу:
print(f'Вместимость вытащенной стопки: {pulled_stack.max_size} шт.')
print(f'Кол-во тарелок в вытащенной стопке: {pulled_stack.stack_size()} шт.')
# А кол-во стопок в шкафу уменьшилось:
print(f'Кол-во стопок в шкафу после вытаскивания последней стопки: {new_shelf.stack_size()} шт.')
print()

# Попробуем переполнить шкаф:
new_shelf.push_in(first_stack, 40)
print(f'Кол-во стопок в шкафу: {new_shelf.stack_size()} шт.')
# Как мы видим, вывелось сообщение, что шкаф переполнен и добавление тарелок и стопок прекратилось
# При этом кол-во стопок в шкафу не стало превышать изначально установленное максимальное

# Проверим, что все стопки при этом заполнены
for i in range(len(new_shelf.stacks)):
    print(f'Вместимость {i + 1}-й стопки: {new_shelf.stacks[i].max_size} шт.')
    print(f'Кол-во тарелок в {i + 1}-й стопке: {new_shelf.stacks[i].stack_size()} шт.')
    print()
print()
