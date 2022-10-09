def mult_scalar(matrix, scale):
	results = []
	for row in range(len(matrix)):
		results.append([])
		for column in range(len(matrix[row])):
			results[row].append([])
			results[row][column] = matrix[row][column] * scale
	return results


def mult_matrix(a, b):
	if len(a[0]) != len(b) or (len(a) < 1) or (len(b) < 1):
		return None
	
	results = []

	row = 0

	for b_column in range(len(b[0])):
		sum = 0
		for a_column in range(len(a[0])):
			sum += a[row][a_column] * b[a_column][b_column]
		results.append(sum)



	# for a_row in range(len(a)):
	# 	results.append([])
	# 	sum = 0

	# 	for b_column in range(len(b[0])):
	# 		for a_column in range(len(a[0])):
	# 			sum += a[a_row][a_column] * b[a_column][b_column]
			
	# 		results[a_row].append(sum)

	return results


	
def euclidean_dist(a,b):
	return -1

a = [
	[1, 2],
	[3, 4]
]

b = [
	[2, 0],
	[1, 2]
]

print(mult_matrix(a, b))