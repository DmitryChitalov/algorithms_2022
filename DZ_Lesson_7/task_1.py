import random

elements = [random.randint(-100, 100) for i in range(100)]


def bubblesort(elements):
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
    elements.reverse()

print(elements)
bubblesort(elements)
print(elements)
