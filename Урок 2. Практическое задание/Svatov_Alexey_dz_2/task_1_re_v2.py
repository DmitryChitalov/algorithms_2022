def mathematics(operator):
	return print(f'Выход из программы') if operator == '0' else return print('Ваш результат: {0}'.format(eval(input('Введите первое число: ')+operator+input('Введите второе число: ')))) mathematics(input('Введите операцию: '))
			
mathematics(input('Введите операцию: '))
			