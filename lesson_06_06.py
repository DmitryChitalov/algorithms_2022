from memory_profiler import profile
# Обернула функцию с рекурсией дополнительной функцией для получения замера

@profile
def num_reverse_rec(number):
    def num_reverse(number, result=''):
        if number == 0:
            return print(result)
        else:
            result += str(number % 10)
        num_reverse(number // 10, result)
    return num_reverse(number, result='')


if __name__ == '__main__':
    num_reverse_rec(12030000)