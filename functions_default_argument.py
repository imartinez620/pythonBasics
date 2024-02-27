def greeting(name = 'Guest'):
	print(f'Hi {name}!')


greeting('Peter')
greeting()


def some_function(collection = []):
	collection.append(1)
	print(id(collection))
	return collection


print(some_function()) #[1]

#other part of the program
print(some_function()) #[1]  is wrong