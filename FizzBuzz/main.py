"""
Write a program that prints the numers from 1 to 'n'.
But for multiples of three print 'Fizz' instead of the number
and for the multiples of five print 'Buzz'.
For numbers which are multiples of both three and five print
'FizzBuzz'.

Use:
- Function
- Looping
- Conditionals
- Math operator
"""

def fizz_buzz(max_number):
	for num in range(1, max_number + 1):
		if num % 3 == 0 and num % 5 == 0:
			print('FizzBuzz')
		elif num % 3 == 0:
			print('Fizz')
		elif num % 5 == 0:
			print('Buzz')
		else:
			print(num) 	
		

fizz_buzz(100)

