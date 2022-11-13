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

	for a_row in range(len(a)):
		results.append([])
		for b_column in range(len(b[0])):
			sum = 0
			for a_column in range(len(a[0])):
				sum += a[a_row][a_column] * b[a_column][b_column]
			results[a_row].append(sum)
	return results


	
def euclidean_dist(a,b):
	sum_of_squares = 0
	for dimension in range(len(a[0])):
		difference = a[0][dimension] - b[0][dimension]
		sum_of_squares += difference**2
	
	return sum_of_squares**(1/2)
