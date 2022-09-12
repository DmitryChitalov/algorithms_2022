"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для пятого скрипта
"""

# Урок 3. Курс Основы.
# Задание 3.
# Шутка - случайная выборка из трех списков.

import random
from memory_profiler import profile
from numpy import array, vectorize, delete
from pympler import asizeof


# __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
@profile
def creating_joke():  # Константы убраны в функцию для замеров.
    NOUNS = ["автомобиль", "лес", "огонь", "город", "дом", "грузовик", "пень", "карандаш", "лес", "потолок", "свет",
             "торт", "стол", "пол", "уголек"]
    print(f'объект list NOUNS занимает {asizeof.asizeof(NOUNS)} байт.')
    ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "днем", "утром", "вечером", "послезавтра",
               "в полдень", "в полночь", "после обеда", "зимой", "летом", "весной"]
    print(f'объект list ADVERBS занимает {asizeof.asizeof(ADVERBS)} байт.')
    ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "соленый", "сладкий", "кислый", "жаркий",
                  "бледный", "белый", "чистый", "простой", "густой", "круглый"]
    print(f'объект list ADJECTIVES занимает {asizeof.asizeof(ADJECTIVES)} байт.')
    #  При использовании списка массив занимает более, чем в 2 раза больше места в памяти, чем
    #  при использовании функции array() из библиотеки NumPy.
    return NOUNS, ADVERBS, ADJECTIVES


# __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
@profile
def creating_joke_arr():
    NOUNS = array(
        ["автомобиль", "лес", "огонь", "город", "дом", "грузовик", "пень", "карандаш", "лес", "потолок", "свет", "торт",
         "стол", "пол", "уголек"])
    print(f'объект array NOUNS занимает {asizeof.asizeof(NOUNS)} байт.')
    ADVERBS = array(["сегодня", "вчера", "завтра", "позавчера", "ночью", "днем", "утром", "вечером", "послезавтра",
                     "в полдень", "в полночь", "после обеда", "зимой", "летом", "весной"])
    print(f'объект array ADVERBS занимает {asizeof.asizeof(ADVERBS)} байт.')
    ADJECTIVES = array(["веселый", "яркий", "зеленый", "утопичный", "мягкий", "соленый", "сладкий", "кислый", "жаркий",
                        "бледный", "белый", "чистый", "простой", "густой", "круглый"])
    print(f'объект array ADJECTIVES занимает {asizeof.asizeof(ADJECTIVES)} байт.')
    #  При использовании функции array() из библиотеки NumPy
    #  массивы стали занимать почти в 2 раза меньше памяти.
    return NOUNS, ADVERBS, ADJECTIVES


# __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
@profile
def get_jokes(sign, repeats, NOUNS, ADVERBS, ADJECTIVES):
    """a random selection of three lists"""
    my_nouns = NOUNS[:]
    print(f'объект list my_nouns занимает {asizeof.asizeof(my_nouns)} байт.')
    my_adverbs = ADVERBS[:]
    print(f'объект list my_adverbs занимает {asizeof.asizeof(my_adverbs)} байт.')
    my_adjectives = ADJECTIVES[:]
    print(f'объект list my_adjectives занимает {asizeof.asizeof(my_adjectives)} байт.')
    if int(sign) == 0:
        print("Да вы шутник!")
    if int(repeats) == 0:
        for i in range(sign):
            del_my_nouns_num = random.randrange(0, len(my_nouns))
            del_my_adverbs_num = random.randrange(0, len(my_adverbs))
            del_my_adjectives_num = random.randrange(0, len(my_adjectives))
            print(
                f'{my_nouns[del_my_nouns_num]}, {my_adverbs[del_my_adverbs_num]}, {my_adjectives[del_my_adjectives_num]}')
            my_nouns.pop(del_my_nouns_num)
            my_adverbs.pop(del_my_adverbs_num)
            my_adjectives.pop(del_my_adjectives_num)
    elif int(repeats) == 1:
        for i in range(sign):
            print(
                f'{NOUNS[random.randrange(0, len(NOUNS))]}, {ADVERBS[random.randrange(0, len(ADVERBS))]}, {ADJECTIVES[random.randrange(0, len(ADJECTIVES))]}')
    else:
        print("Проверьте ввод")
    print(f'объект list my_nouns занимает {asizeof.asizeof(my_nouns)} байт.')
    print(f'объект list my_adverbs занимает {asizeof.asizeof(my_adverbs)} байт.')
    print(f'объект list my_adjectives занимает {asizeof.asizeof(my_adjectives)} байт.')


# __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
@profile
def get_jokes_arr(sign, repeats, nouns_arr, adverbs_arr, adjectives_arr):
    """a random selection of three lists"""
    # при испльзовании функцию array() из библиотеки NumPy
    # срезы массивов тоже стали занимать практически в 2 раза меньше памяти.
    my_nouns = nouns_arr[:]
    print(f'объект array my_nouns занимает {asizeof.asizeof(my_nouns)} байт.')
    my_adverbs = adverbs_arr[:]
    print(f'объект array my_adverbs занимает {asizeof.asizeof(my_adverbs)} байт.')
    my_adjectives = adjectives_arr[:]
    print(f'объект array my_adjectives занимает {asizeof.asizeof(my_adjectives)} байт.')
    if int(sign) == 0:
        print("Да вы шутник!")
    if int(repeats) == 0:
        for i in range(sign):
            del_my_nouns_num = random.randrange(0, my_nouns.size)
            del_my_adverbs_num = random.randrange(0, my_adverbs.size)
            del_my_adjectives_num = random.randrange(0, my_adjectives.size)
            print(
                f'{my_nouns[del_my_nouns_num]}, {my_adverbs[del_my_adverbs_num]}, {my_adjectives[del_my_adjectives_num]}')
            delete(my_nouns, del_my_nouns_num)
            delete(my_adverbs, del_my_adverbs_num)
            delete(my_adjectives, del_my_adjectives_num)
    elif int(repeats) == 1:
        for i in range(sign):
            print(
                f'{nouns_arr[random.randrange(0, nouns_arr.size)]}, {adverbs_arr[random.randrange(0, adverbs_arr.size)]}, {djectives_arr[random.randrange(0, djectives_arr.size)]}')
    else:
        print("Проверьте ввод")
    #  Присвоение переменной вместо срезов значения None
    #  ведет к уменьшению используемой памяти почти в 50 раз.
    my_nouns = None
    print(f'объект None array my_nouns занимает {asizeof.asizeof(my_nouns)} байт.')
    my_adverbs = None
    print(f'объект None array my_adverbs занимает {asizeof.asizeof(my_adverbs)} байт.')
    my_adjectives = None
    print(f'объект None array my_adjectives занимает {asizeof.asizeof(my_adjectives)} байт.')


if __name__ == '__main__':
    @profile  # Исполнение скрипта помещено в функцию для производства замеров.
    # __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
    def joke():
        sign = None
        repeats = None
        sign = input("Скоько желаете шуток? (введите число от 1 до 5)? ")
        repeats = input("Есть повторы? (Да - 1, Нет - 0) ")
        my_nouns, my_adverbs, my_adjectives = creating_joke()
        try:
            get_jokes(int(sign), int(repeats), my_nouns, my_adverbs, my_adjectives)
        except:
            print("Проверьте ввод")


    @profile
    # __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
    def joke_arr():
        sign = input("Скоько желаете шуток? (введите число от 1 до 5)? ")
        repeats = input("Есть повторы? (Да - 1, Нет - 0) ")
        my_nouns_arr, my_adverbs_arr, my_adjectives_arr = creating_joke_arr()
        try:
            get_jokes_arr(int(sign), int(repeats), my_nouns_arr, my_adverbs_arr, my_adjectives_arr)
        except:
            print("Проверьте ввод")


    # Использование декоратора @profiler из профилировщика memory_profiler
    # проблем с использованием памяти при работе скрипта не выявляет (мал объем данных).
    # Increment везде 0. Значение Mem usage не меняетя.

    # __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
    joke()
    # __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
    joke_arr()
