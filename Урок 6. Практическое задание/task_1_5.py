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

"""
В качестве примера выбрана 5 задача из 3 урока по Основам python
"""


import random
from pympler import asizeof

# исходный код
def get_jokes(count, repeat=True, **kwargs) -> list:
    list_out = []
    if repeat == True:
        for i in range(count):
            list_out.append(' '.join(random.choice(kwargs[j]) for j in kwargs.keys()))
    elif repeat == False:
        for i in range(count):
            noun, adverb, adjective = [random.choice(kwargs[j]) for j in kwargs.keys()]
            list_out.append(' '.join([noun, adverb, adjective]))
            kwargs['nouns'].remove(noun)
            kwargs['adverbs'].remove(adverb)
            kwargs['adjectives'].remove(adjective)

    return list_out

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# оптимизированный код

def create_joke(count, **kwargs):
    ww = 0
    for j in kwargs.keys():
        if ww < 2:
            print(f'{random.choice(kwargs[j])}', end=' ')
            ww += 1
        else:
            print(f'{random.choice(kwargs[j])}')

def get_jokes_1(count, repeat=True) -> list:
    if repeat:
        for i in range(count):
            create_joke(count, nouns=nouns, adverbs=adverbs, adjectives=adjectives)

    elif not repeat:
        dict_jokes = dict(nouns=nouns, adverbs=adverbs, adjectives=adjectives)
        for i in range(count):
            noun, adverb, adjective = (random.choice(dict_jokes[j]) for j in dict_jokes.keys())
            print(f'{noun} {adverb} {adjective}')
            dict_jokes['nouns'].remove(noun)
            dict_jokes['adverbs'].remove(adverb)
            dict_jokes['adjectives'].remove(adjective)

print(asizeof.asized(get_jokes(4, nouns=nouns, adverbs=adverbs, adjectives=adjectives), detail=1).format())
print(asizeof.asized(get_jokes_1(4), detail=1).format())

"""
Для оптимизации избавился от создания списка в функции и использовал f-строки для вывода
Вынес отдельно функцию генерирования шутки (при repeat=True),
чтобы не передавать в функцию именованные аргументы в kwargs, а только число и флаг.
По профилированию можно посмотреть что было создано и какого оно размера.

До оптимизации:
['город позавчера веселый', 'лес сегод....д вчера веселый', 'дом ночью веселый'] size=552 flat=88
    'город позавчера веселый' size=120 flat=120
    'лес сегодня утопичный' size=120 flat=120
    'город вчера веселый' size=112 flat=112
    'дом ночью веселый' size=112 flat=112

После оптимизации:
город завтра утопичный
дом вчера мягкий
огонь завтра веселый
город завтра утопичный
None size=16 flat=16

За счёт того, что не создаётся куча новых объектов, экономим память
"""