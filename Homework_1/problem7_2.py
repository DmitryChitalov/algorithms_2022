from problem7_1 import Deque
def bs(phrase):
    big_word = Deque()
    for letter in ''.join(phrase.split()):
        big_word.back_add(letter)
    equality = True
    while big_word.lenght() >= 2 and equality:
        a = big_word.front_remove()
        b = big_word.back_remove()
        if a != b:
            equality = False
            break
    return equality

print(bs('молоко делили ледоколом'))