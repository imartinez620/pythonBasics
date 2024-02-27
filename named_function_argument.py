def full_name(first, last):
	return f'{first} {last}'


peter = full_name(first = 'Peter', last = 'Parker')
print(peter)

peter = full_name(last = 'Parker', first = 'Peter')
print(peter)