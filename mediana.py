import math
"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

number_of_elements = len(sale_prices)
sale_prices.sort()

if number_of_elements % 2 != 0:
  number_of_index_of_mediana = math.floor(number_of_elements / 2)
  print(sale_prices[number_of_index_of_mediana])


print(number_of_elements)
print(sale_prices)

#Solution
sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:]
last_sales_items = sorted_list[-half_slice:]
median = sorted_list[half_slice:half_slice+1]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)


