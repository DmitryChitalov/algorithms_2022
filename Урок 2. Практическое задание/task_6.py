"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

def random_number(randomNumber, counter=0):

    if counter == 10:
        return 'Ваши 10 попыток истекли, правильный ответ: {}...'.format(ranNumber)

    number = int(raw_input('Введите ваше число: '))

    if number == randomNumber:
        return 'Поздравляем! Вы угадали! Правильный ответ {}!!!'.format(number)

    if int(number) > int(randomNumber):
        print 'Ответ не верный, ваше число больше ...'
        counter += 1
        
        return random_number(randomNumber=randomNumber, counter=counter)

    if int(number) < int(randomNumber):
        print 'Ответ не верный, ваше число меньше ...'
        counter += 1
        
        return random_number(randomNumber=randomNumber, counter=counter)
        
        
if __name__ == '__main__':
    ranNumber = random.randrange(0, 100)
    print random_number(randomNumber=int(ranNumber))
