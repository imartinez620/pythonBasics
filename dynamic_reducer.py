import operator
from functools import reduce

"""
dynamic_reducer([1,2,3], '+') #6
dynamic_reducer([1,2,3], '-') #-4
dynamic_reducer([1,2,3], '*') #6
dynamic_reducer([1,2,3], '/') #1/6
"""

def dynamic_reducer(lista_operadores, operator):
	if operator == '+':
		result = reduce(lambda x, y: x+y, lista_operadores)
	elif operator == '-':
		result = reduce(lambda x, y: x-y, lista_operadores)
	elif operator == '*':
		result = reduce(lambda x, y: x*y, lista_operadores)
	elif operator == '/':
		result = reduce(lambda x, y: x/y, lista_operadores)

	
	print(result)

dynamic_reducer([2,4,3], '+')
dynamic_reducer([2,4,3], '-')
dynamic_reducer([2,4,3], '*')
dynamic_reducer([2,4,3], '/')

#Solution
def dynamic_reducer2(collection, op):
	operators = {
		"+": operator.add,
		"-": operator.sub,
		"*": operator.mul,
		"/": operator.truediv
	}

	return reduce(lambda total,element: operators[op](total, element), collection)

print(dynamic_reducer2([2,3,4], '+'))
print(dynamic_reducer2([2,3,4], '-'))
print(dynamic_reducer2([2,3,4], '*'))
print(dynamic_reducer2([2,3,4], '/'))