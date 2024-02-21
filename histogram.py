"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

histogram = {
	'g':20,
	'f':42,
	't':10,
	'o':12,
}

def return_histogram(key):
	number = histogram.get(key, 0)

	print(key + ' ' + number * '$')

return_histogram('g')
return_histogram('f')
return_histogram('t')
return_histogram('o')
return_histogram('j')

#solution
sales = {
	'google':20,
	'facebook':42,
	'twitter':10,
	'offline':12,
}

print('g ' + sales['google'] * '$')
print('f ' + sales['facebook'] * '$')
print('t ' + sales['twitter'] * '$')
print('o ' + sales['offline'] * '$')