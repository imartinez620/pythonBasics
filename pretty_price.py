# pretty_price(3.20, 99) > 3.99
# pretty_price(3.20, 0.99) > 3.99
import math 

def pretty_price(price, round):
	result = math.floor(price)
	if round < 1 and round > 0:
		result += round
	elif round > 1:
		result += round/100
	return result

print(pretty_price(3.5, 99))
print(pretty_price(3.20, 9))
print(pretty_price(3.25, 90))
print(pretty_price(3.5, 0.99))

#Solution
def pretty_price_solution(price, round):
	if isinstance(round, int):
		round = round * 0.01
	return int(price) + round

print(pretty_price_solution(3.5, 99))
print(pretty_price_solution(3.20, 9))
print(pretty_price_solution(3.25, 90))
print(pretty_price_solution(3.5, 0.99))

