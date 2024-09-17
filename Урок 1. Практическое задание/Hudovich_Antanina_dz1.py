Задание 1

def check_1(lst_obj):
    """Функция должна создать множество из списка.
    Алгоритм 1:
    Создать множество из списка
    Сложность: O(n) - линейная
    """
    lst_to_set = set(lst_obj)  # O(n) - линейная
    return lst_to_set  # O(1) - константная

##############################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 2:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах
    Сложность: O(n^2)- квадратичная.
    """
    for j in range(len(lst_obj)):          # O(n) - линейная
        if lst_obj[j] in lst_obj[j+1:]:    # O(n) - линейная
            return False                   # O(1) - константная
    return True                            # O(1) - константная


##############################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 3:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: n + n log n + n(1 + 1) + 1  - O(n log n)- линейно-логарифмическая
    """
    lst_copy = list(lst_obj)                 # O(n) - линейная
    lst_copy.sort()                          # O(n log n) - линейно-логарифмическая
    for i in range(len(lst_obj) - 1):        # O(n) - линейная
        if lst_copy[i] == lst_copy[i+1]:     # O(1) - константная
            return False                     # O(1) - константная
    return True                              # O(1) - константная


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)


"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""
our_list = [13, 188,  21, 6, -10, 50, -22]
min_val = our_list[0]
for i in range(len(our_list)):    # O(n)
    if our_list[i] < min_val:     # O(1)
        min_val = our_list[i]     # O(1)
print(min_val)  # итого линейная

min_val2 = our_list[0]
for i in our_list:                # O(n)
    if i < min_val2:              # O(1)
        for j in our_list[i:]:    # O(n)
            if i > j:             # O(1)
                min_val2 = j
            else:
                min_val2 = i

print(min_val2)   # итого квадратичная






"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
companies_to_sort = {
    'capitan_jack_corporation': 777777,
    'elizabeth_swann_bank': 555555,
    'will_turner_prison': 111111,
    'blue_parrot_granary': 333333
}
list_to_sort = []                                   # O(1)
for val in companies_to_sort.values():          # O(n)
    list_to_sort.append(val)                           # O(1)
list_to_sort.sort(reverse=True)                      # O(n logn)
top3 = list_to_sort[0:3]                          # O(1)
for key in companies_to_sort.keys():                   # O(n)
    if companies_to_sort[key] in top3:                # O(n)
        print(key)                                    # O(1)
# Итоговая сложность O(n^2) - здесь часть про ключ для вывода именно названия компаний,
# ну и без нее сложность одинаковая. Разбор посмотрела, возник вопрос,
# параллельное присваивание все равно имеет константную сложность?


companies = list(companies_to_sort.items())               # O(1)
sorted_companies = sorted(companies, key=lambda el: el[1], reverse=True)   # O(n logn)
print(sorted_companies[:3])                  # O(1)

# Итоговая сложность O(n logn) - решение более эффективно



"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
users_list = {
    'user_a': 1111,
    'user_a_activated': True,
    'user_b': 2222,
    'user_b_activated': False,
    'user_c': 3333,
    'user_c_activated': False
}


def authentication(users):
    name = input('Введите логин: ')         # O(1)
    if name in users.keys():                 # O(n)
        password = int(input('Введите пароль: '))    # O(1)
        activation = name + '_activated'             # O(1)
        if password == users[name] and users[activation]:  # O(1)
            return print('Все в порядке. доступ разрешен')
        elif password == users[name] and users[activation] is False:   # O(1)
            return print('Пароль верный, но вaм нужно пройти активацию')
        else:
            return print('Пароль неверный')
    else:
        return print('Пользователь с таки именем не зарегистрирован')


authentication(users_list)    # O(n)


def authentication_1(users):
    name = input('Введите логин: ')         # O(1)
    try:
        password = int(input('Введите пароль: '))    # O(1)
        activation = name + '_activated'             # O(1)
        if password == users[name] and users[activation]:  # O(1)
            return print('Все в порядке. доступ разрешен')
        elif password == users[name] and users[activation] is False:   # O(1)
            return print('Пароль верный, но вaм нужно пройти активацию')
        else:
            return print('Пароль неверный, доступ запрещен')
    except KeyError:
        print('Имя пользователя не зарегистрировано, доступ запрещен')


authentication_1(users_list)   # O(1) - это решение более эффективно





"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""

class Stack:
    def __init__(self, sub_len):
        self.elems = [[]]
        self.sub_len = sub_len

    def put_in_stack(self, *args):
        for arg in args:
            if len(self.elems[len(self.elems) - 1]) == self.sub_len:
                self.elems.append([])
            self.elems[len(self.elems) - 1].append(arg)

    def get_from_stack(self):
        element = self.elems[len(self.elems) - 1].pop()
        if len(self.elems[-1]) == 0:
            self.elems.pop()
        return element

    def show(self):
        return print(self.elems)

    def length(self):
        return print(len(self.elems))


if __name__ == '__main__':
    stack_b = Stack(2)

    stack_b.put_in_stack('lala', 'dfkjhk', 'frfrfrf', 'jijijij', 'ccc', 'ggg', 'eeee')
    stack_b.put_in_stack('rrr')
    stack_b.get_from_stack()
    stack_b.show()  # [['lala', 'dfkjhk'], ['frfrfrf', 'jijijij'], ['ccc', 'ggg'], ['eeee']]
    stack_b.get_from_stack()
    stack_b.show()  # [['lala', 'dfkjhk'], ['frfrfrf', 'jijijij'], ['ccc', 'ggg']]
    stack_b.length()  # 3




"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

class Queue:
    def __init__(self):
        self.elems = []

    def add_task(self, task):
        return self.elems.insert(0, task)

    def get_task(self):
        return self.elems.pop()

    def move_task(self, to_queue):
        return to_queue.add_task(self.elems.pop())

    def show(self):
        return print(self.elems)


class TaskBoard:
    def __init__(self):
        self.tasks = Queue()
        self.fix = Queue()
        self.ready = []

    def add_task_to_board(self, *args):
        for arg in args:
            self.tasks.add_task(arg)

    def to_process(self):
        return self.ready.append(self.tasks.get_task())

    def to_fix(self):
        return self.tasks.move_task(self.fix)

    def show_board(self):
        return print('our tasks: ', end=''), self.tasks.show(), print('we have to fix: ', end=''), self.fix.show(), \
               print('ready: ', self.ready)


if __name__ == '__main__':
    board = TaskBoard()
    board.add_task_to_board('some work1', 'work', 'work work', 'hard work')
    board.show_board()
# our tasks: ['hard work', 'work work', 'work', 'some work1']
# we have to fix: []
# ready:  []

    board.to_process()
    board.to_process()
    board.to_fix()

    board.show_board()
# our tasks: ['hard work']
# we have to fix: ['work work']
# ready:  ['some work1', 'work']

# Надеюсь правильно поняла, как должны были двигаться задачи


"""
Задание 7. На закрепление навыков работы с деком
В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов,
например, 'топот'
Но могут быть и такие палиндромы, как 'молоко делили ледоколом'
Вам нужно доработать программу так, чтобы она могла выполнить
проверку на палиндром
и в таких строках (включающих пробелы)
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--код с нуля писать не нужно, требуется доработать пример с урока
"""

# палиндром

from task_14 import DequeClass


def pal_checker(string):
    dc_obj = DequeClass()

    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first == ' ':
            first = dc_obj.remove_from_front()
        elif last == ' ':
            last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False
    return still_equal


print(pal_checker("молоко делили ледоколом"))

# Хотела попробовать обработать разное количество пробелов,
# но  while внутри другого while вызывал ошибку. пока не разобралась,почему