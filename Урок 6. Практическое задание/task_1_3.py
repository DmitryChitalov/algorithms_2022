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

Это файл для третьего скрипта
"""
# из курса основ урок 3 задание 5
# генератор шуток

from random import choice, randrange
from memory_profiler import memory_usage


def memory_counter(func):
    def wrapper(*args):
        start = memory_usage(include_children=True)[0]
        result = func(*args)
        end = memory_usage(include_children=True)[0]
        memory_used = end - start
        print('Использовано памяти:', memory_used)
        return result
    return wrapper


@memory_counter
def get_jokes(number, flag=False):
    """
    Генератор шуток
    :number: количество шуток
    :flag: возможность повтора слов
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "странный"]
    jokes = []
    if flag:
        for i in range(number):
            joke = f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
            jokes.append(joke)
    else:
        if number > min(len(nouns), len(adverbs), len(adjectives)):
            return f"Максимум {min(len(nouns), len(adverbs), len(adjectives))} загадок"
        else:
            for i in range(number):
                joke = f"{nouns.pop(randrange(len(nouns)))} {adverbs.pop(randrange(len(adverbs)))}" \
                       f" {adjectives.pop(randrange(len(adjectives)))}"
                jokes.append(joke)
    return jokes


@memory_counter
def jokes_generator(number, flag=False):
    """
    Генератор шуток
    :number: количество шуток
    :flag: возможность повтора слов
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "странный"]
    if flag:
        for i in range(number):
            yield f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
    else:
        if number > min(len(nouns), len(adverbs), len(adjectives)):
            return f"Максимум {min(len(nouns), len(adverbs), len(adjectives))} загадок"
        else:
            for i in range(number):
                yield f"{nouns.pop(randrange(len(nouns)))} {adverbs.pop(randrange(len(adverbs)))}" \
                       f" {adjectives.pop(randrange(len(adjectives)))}"


if __name__ == '__main__':
    number_of_jokes = 3
    for joke in get_jokes(number_of_jokes, True):
        print(joke)
    print('**********************')

    for joke in jokes_generator(number_of_jokes, True):
        print(joke)

# Использовано памяти: 0.04296875
# огонь когда-то мягкий
# огонь вчера веселый
# дом когда-то яркий
# **********************
# Использовано памяти: 0.00390625
# лес когда-то странный
# автомобиль когда-то веселый
# огонь сегодня яркий

# Применение генератора позволило сильно сократить потребление памяти
