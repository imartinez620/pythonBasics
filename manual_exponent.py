from functools import reduce
"""
manual_exponent(2, 3)
#> 8

manual_exponent(10, 2)
#> 100
"""

#Option 1: Iterative
def manual_exponent_it(base, exponent):
	if exponent == 0:
		return 1
	elif exponent == 1:
		return base
	else:
		return base * manual_exponent_it(base, exponent-1)

#Option 2: Reducer
def manual_exponent_red(base, exponent):
	result = reduce(lambda x,y: x**y, (base, exponent))
	return result

print(manual_exponent_it(5, 4))
print(manual_exponent_red(5, 4))

#Solution
#Option 1: Iterative
def manual_exponent_it_sol(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

#Option 2: Reducer
def manual_exponent_red_sol(base, exponent):
	computed_list = [base] * exponent
	print(computed_list)
	result = reduce(lambda total,element: total * element, computed_list)
	return result

print(manual_exponent_it_sol(5, 4))
print(manual_exponent_red_sol(5, 4))