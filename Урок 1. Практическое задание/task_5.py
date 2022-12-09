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


class StackClass:
    """Класс "Хранилище тарелок". Экземпляр класса наполняется "тарелками" - любыми произвольными элементами или
    данными. Новые элементы помещаются в "стопку". Если количество элементов в "стопке" достигает 5, наполнение
    переключается на следующую "стопку". Количество "стопок" не ограничено."""

    def __init__(self):
        self.input_stack = list()
        self.output_stack = list()
        self.i = 1

    def push(self, el):
        self.input_stack.append(el)
        substack = list()
        for k in range(len(self.input_stack) - self.i, len(self.input_stack)):
            substack.append(self.input_stack[k])
        if self.i == 1:
            self.output_stack.append(substack)
        else:
            self.output_stack[len(self.output_stack) - 1] = substack
        if self.i == 5:
            self.i = 1
        else:
            self.i += 1

    def to_pull(self):  # Добавлен метод удаления элементов (принцип LIFO).
        substack = self.output_stack.pop()
        to_output = substack.pop()
        if len(substack) > 0:
            self.output_stack.append(substack)
        return to_output


user_stack = StackClass()
for i in range(1, 14):
    user_stack.push(f'Тарелка №{i}')
print(user_stack.output_stack)
for _ in range(1, 7):
    user_stack.to_pull()
print(user_stack.output_stack)
