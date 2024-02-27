def full_name(first, last):
	print(f'Hi {first} {last}')


full_name('Peter','Parker')


def auth(email, password):
	if email == 'kris@eusk.com' and password == 'secret':
		print('Authorized')
	else:
		print('Not autoriced')


auth('kris@eusk.com', 'secret')
auth('tom@eusk.com', 'secret')


def hundred():
	for num in range(1,10):
		print(num)


hundred()


def hundred(max_value):
	for num in range(1,max_value):
		print(num)


hundred(15)
