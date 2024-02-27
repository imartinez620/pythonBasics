def greeting(*args):
	print('Hi ' + ' '.join(args))


greeting('Peter', 'Parker')
greeting('Peter', 'P.', 'Parker')


def greeting(time_of_the_day, *args):
	print(f"Hi {' '.join(args)} this {time_of_the_day}")


greeting('morning','Peter', 'Parker')
greeting('afternoon', 'Peter', 'P.', 'Parker')
