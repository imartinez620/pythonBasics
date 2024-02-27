def full_name(first, last):
	return f'{first} {last}'


peter = full_name('Peter','Parker')


def greeting(name):
	print(f'Hi {name}!')


greeting(peter)


print("###################")


def greeting(first, last):
	def full_name():
		return f'{first} {last}'


	print(f'Hi {full_name()}!')


greeting('Peter', 'Parker')