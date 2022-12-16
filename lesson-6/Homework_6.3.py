from memory_profiler import memory_usage
import random


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# 5. Реализовать функцию get_jokes()
# @decor
# def get_jokes_1(number):
#     nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#     adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#     adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#     jokes = []
#     for i in range(number):
#         joke = nouns[random.randint(0, len(nouns) - 1)] + ' ' + adverbs[random.randint(0, len(adverbs) - 1)] + ' ' + \
#                adjectives[random.randint(0, len(adjectives) - 1)]
#         jokes.append(joke)
#     return jokes
#
#
# jokes_1, mem1 = get_jokes_1(10**5)
# print(mem1)
#  Выполнение заняло 13.51171875 Mib

# Заменим списки на кортежи, сделаем генератор, используем f-строку
@decor
def get_jokes_2(number):
    nouns = ("автомобиль", "лес", "огонь", "город", "дом")
    adverbs = ("сегодня", "вчера", "завтра", "позавчера", "ночью")
    adjectives = ("веселый", "яркий", "зеленый", "утопичный", "мягкий")
    for _ in range(number):
        yield f'{nouns[random.randint(0, len(nouns) - 1)]} {adverbs[random.randint(0, len(adverbs) - 1)]} ' \
              f'{adjectives[random.randint(0, len(adjectives) - 1)]} '


jokes_2, mem2 = get_jokes_2(10**3)
for j in jokes_2:
    print(j)
print(mem2)
# Выполнение заняло 0.00390625 Mib