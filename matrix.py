"""
[
	[0,1,2,3,4],
	[1,2,3,4,5],
	[2,3,4,5,6],
	[3,4,5,6,7],
	[4,5,6,7,8]
]
"""

def manual_incrementing_matrix(value):
	#matrix n x n
	matrix = [[0 for y in range(value)] for x in range(value)]
	counter = 0

	for idx, el in enumerate(matrix):

		for nested_idx, nested_el in enumerate(el):
			matrix[idx][nested_idx]= counter + nested_idx + idx

	return matrix

print(manual_incrementing_matrix(4))
