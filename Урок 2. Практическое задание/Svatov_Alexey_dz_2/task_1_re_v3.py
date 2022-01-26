def mathematics(operator):
	(return print(f'Выход из программы'), [return 'Ваш результат: {0}'.format(eval(input('Введите первое число: ')+operator+input('Введите второе число: '))), mathematics(input('Введите операцию: '))])[operator == '0']
			
mathematics(input('Введите операцию: '))
			