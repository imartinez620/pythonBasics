def greeting(**kwargs):
	if kwargs:
		print(f"Hi {kwargs['first_name']} {kwargs['last_name']}") # imprime un diccionario
	else:
		print("Hi guest")

greeting(first_name = 'Peter', last_name = 'Parker')
greeting()