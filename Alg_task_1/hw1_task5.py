class StackClass:
    # дописана функция __str__
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        self.elems.append(el)

    def pop_out(self):
        return self.elems.pop()

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def stack_size(self):
        return len(self.elems)

    def __str__(self):   # дописал функцию для визуализации стэков
        res = ''
        for value in self.elems:
            res = res + f'{value} '
        res = '[ ' + res + ']'
        return res


def plates_str(name_stack: StackClass, i, limitations):
    """
    :param name_stack: по сути стэк из стэков
    :param i: номер создаваемого стэка
    :param limitations: ограничение по тому сколько тарелок можно добавить
     к новому стэку (в моем случае в новый стэк можно доложить всего 3 тарелки и дальше
      создавать новый)
     Реализовал функцию через рекурсию
     Цифрами в выводе характеризуются номера тарелок
    """
    if i < 5:  # регулируемый параметр, но для наглядности взял 4 стопки
        if name_stack.is_empty() == 0:
            sub_stack = plates_sub(name_stack)  # получаем последний стэк
            # в перевернутом виде
            k = sub_stack.stack_size()
            for t in range(k+1, k+limitations+1):  # Заполняем стопку тарелками
                sub_stack.push_in(t)
            name_stack.push_in(sub_stack)
        else:  # ветка срабатывает лишь в 1-ый раз
            sub_stack = StackClass()
            for k in range(i, limitations + 1):
                sub_stack.push_in(k)
            name_stack.push_in(sub_stack)
        print(f'шаг {i} стэк имеет вид: ', name_stack)  # цифра - номер тарелки
        plates_str(name_stack, i+1, limitations)


def plates_sub(name_stack: StackClass):
    """
    :param name_stack: наш стэк стэков, но работаем лишь с его последним значением.
    Когда стопка заполнена, то тарелки достаем сверху вниз для заполнении новой.
    Поэтому если было расположение "123", то станет "321", где цифры-номера тарелок.
    Перевернутное последнее значение стэка(из стэков) возвращается через return.
    Соответственно предыдущие стэки обнуляются.
    """
    sub_stack = name_stack.get_val()  # последнее значение стэка
    sub_sub_stack = StackClass()  # будет перевернутый последний стэк
    while sub_stack.is_empty() == 0:
        sub_sub_stack.push_in(sub_stack.pop_out())
    return sub_sub_stack


plate = StackClass()
plates_str(plate, 1, 3)
