"""
комментарий после проверки:
не прочитан текст ДЗ
print(reverse_number(1230)) - > 321
"""


# неправильно поняла с нулями и целеноправленно их вырезала, убрала этот кусок кода

def reverse_number(num):
    if num // 10 > 0:
        print(num % 10, end='')
        return reverse_number(num // 10)
    else:
        return num % 10


print(reverse_number(123))
print(reverse_number(1230))
print(reverse_number(12345))
print(reverse_number(4890000))
