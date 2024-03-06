from functools import reduce
"""
num_list = [1,2,3,4,5,6]
mean(num_list) > sum(values)/len
""" 

num_list = [1,2,3,4,5,6]

def do_mean(numbers):
	return reduce(lambda x,y: x+y, numbers) / len(num_list)


print(do_mean(num_list))

# Solution
def get_average(list):
    total = reduce((lambda total, element: total + element), list)
    return total / len(list)


avg = get_average([1, 2, 3, 4, 5, 6])

print(avg)