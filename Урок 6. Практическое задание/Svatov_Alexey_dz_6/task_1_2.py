"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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

Это файл для второго скрипта
"""

# basics_Урок 3. task_5

from random import shuffle
from memory_profiler import profile
from numpy import array


@profile
def get_jokes(n=10000):
    """Create n-jokes from 3 lists and return list of jokes"""
    list_jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"] * n
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"] * n
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"] * n
    shuffle(nouns)
    shuffle(adverbs)
    shuffle(adjectives)
    for noun, adverb, adjective in zip(nouns[:n], adverbs[:n], adjectives[:n]):
        list_jokes.append(' '.join([noun, adverb, adjective]))
    return list_jokes


@profile
def get_jokes_v2(n=10000):
    """Create n-jokes from 3 lists and return list of jokes"""
    list_jokes = []
    nouns = array(["автомобиль", "лес", "огонь", "город", "дом"] * n)
    adverbs = array(["сегодня", "вчера", "завтра", "позавчера", "ночью"] * n)
    adjectives = array(["веселый", "яркий", "зеленый", "утопичный", "мягкий"] * n)
    shuffle(nouns)
    shuffle(adverbs)
    shuffle(adjectives)
    for noun, adverb, adjective in zip(nouns[:n], adverbs[:n], adjectives[:n]):
        list_jokes.append(' '.join([noun, adverb, adjective]))
    return array(list_jokes)


@profile
def get_jokes_v3(n=10000):
    """Create n-jokes from 3 lists and return list of jokes"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"] * n
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"] * n
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"] * n
    shuffle(nouns)
    shuffle(adverbs)
    shuffle(adjectives)
    return [f'{noun} {adverb} {adjective}' for noun, adverb, adjective in zip(nouns[:n], adverbs[:n], adjectives[:n])]


get_jokes()
get_jokes_v2()
get_jokes_v3()

"""
Исходное решение модифицировано для большего удобства работы и наглядности: убран print результата функции, 
                                                                            n не вводится отдельно и равен 10000,
                                                                            размеры списов умножаются на n.
                                                                            
В v2 применён array из numpy, но такой подход требует большего объёма памяти, чем первоначальное решение.
В v3 применена f-строка и lc.
В итоге разница между результатом выполнения функции и стартом:
    v1: 35.9 - 33.3 = 2.6
    v2: 41.3 - 34.9 = 6.4
    v3: 36.0 - 34.9 = 1.1
"""
