while True:
	znak = input('Выберите операцию: ')
	print('Привет, я кадькулятор')
	if znak not in ['-','*','+','/']:
		print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
		break
	elif znak == '+':
		otvet = 0
		formula = ''
		how_match = int(input('Сколько операндов? '))
		for i in range(1, how_match + 1):
			digit = int(input(f'Введите {i} операнд: '))
			otvet += digit
			if i == how_match:
				formula += str(digit)
			else:	
				formula += str(digit) + ' ' + znak + ' '
		print(f'{formula} = {otvet}')
	elif znak == '-':
		formula = ''
		how_match = int(input('Сколько операндов? '))
		for i in range(1, how_match + 1):
			digit = int(input(f'Введите {i} операнд: '))
			if i == 1:
				otvet = digit
				formula += str(digit) + ' ' + znak + ' '
			elif i == how_match:
				otvet -= digit
				formula += str(digit)
			else:
				otvet -= digit	
				formula += str(digit) + ' ' + znak + ' '
		print(f'{formula} = {otvet}')
	elif znak == '*':
		formula = ''
		how_match = int(input('Сколько операндов? '))
		for i in range(1, how_match + 1):
			digit = int(input(f'Введите {i} операнд: '))	
			if i == 1:
				otvet = digit
				formula += str(digit) + ' ' + znak + ' '
			elif i == how_match:
				otvet *= digit
				formula += str(digit)
			else:
				otvet *= digit	
				formula += str(digit) + ' ' + znak + ' '
		print(f'{formula} = {otvet}')
	else:
		formula = ''
		how_match = int(input('Сколько операндов? '))
		for i in range(1, how_match + 1):
			digit = int(input(f'Введите {i} операнд: '))	
			if i == 1:
				otvet = digit
				formula += str(digit) + ' ' + znak + ' '
			elif i == how_match:
				otvet /= digit
				formula += str(digit)
			else:
				otvet /= digit	
				formula += str(digit) + ' ' + znak + ' '
		print(f'{formula} = {otvet}')
			


			





