def mathematics():
	operator = input('Введите операцию: ')
	operators = ['0', '+', '-', '*', '/']
	if operator in operators:
		if operator == '0':
			return print(f'Выход из программы')
		else:
			v_1 = input('Введите первое число: ')
			v_2 = input('Введите второе число: ')
			return print(f'Ваш результат: {eval(v_1+operator+v_2)}'), mathematics()
			
mathematics()
			