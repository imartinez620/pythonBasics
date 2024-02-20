import numpy as np

weights = {
	'winning': 1,
	'losing': 1000
}

other_weights = {
	'winning': 1,
	'break_even': 2,
	'losing': 3
}

def weighted_lottery(var_weights):
	container_list = []
    
	for (name,weight) in var_weights.items():
		for _ in range(weight):
			container_list.append(name)

	return np.random.choice(container_list)

print(weighted_lottery(weights))
print(weighted_lottery(other_weights))