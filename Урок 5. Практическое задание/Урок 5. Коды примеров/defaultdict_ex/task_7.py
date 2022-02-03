"""подсчет слов в предложении"""

from collections import defaultdict

SENTENCE = "Ехал Грека через реку, Видит Грека — в реке рак " \
           "Сунул Грека руку в реку — рак не цапает никак!"
WORDS = SENTENCE.split(' ')


def test_simple_dict():
    """Обычный словарь"""
    reg_dict = {}
    for word in WORDS:
        if word in reg_dict:
            reg_dict[word] += 1
        else:
            reg_dict[word] = 1
    return reg_dict


""" defaultdict автоматически назначает ноль как значение любому ключу, 
который еще не имеет значения. Мы добавили одно, так что теперь в нем больше смысла,
и оно также будет увеличиваться, если слово повторяется в 
предложении несколько раз в предложении."""


def test_default_dict():
    """Вариант с defaultdict"""
    d = defaultdict(int)
    for word in WORDS:
        d[word] += 1
    return d
