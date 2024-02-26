#https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/introduction-using-list-comprehension-python


num_list = range(1,11)
cubed_nums = []

for num in num_list:
	cubed_nums.append(num ** 3)

print(list(num_list))
print(cubed_nums)
print('############################')

cubed_nums = [num ** 3 for num in num_list]

print(list(num_list))
print(cubed_nums)
print('############################')

even_numbers = []
for num in num_list:
	if num % 2 == 0:
		even_numbers.append(num)

print(list(num_list))
print(even_numbers)
print('############################')

even_numbers = [num for num in num_list if num % 2 == 0]
print(list(num_list))
print(even_numbers)
