# swap numbers
def swap(i, j, k, l):
	temp = matrix[i][j]
	matrix[i][j] = matrix[k][l]
	matrix[k][l] = temp
	
	
# create matrix of size N
def initialize_matrix(N):
	
	matrix = [[0 for x in range(N)] for y in range(N)]
	counter = 0
	
	for i in range(N):
		for j in range(N):
			matrix[i][j] = counter
			counter += 1
			
	return matrix


# display matrix on screen
def display_matrix(matrix):

	print()
	for i in range(N):
		for j in range(N):
			if matrix[i][j] < 10: # added to make matrix look better when numbers are two digits
				print(str(matrix[i][j]) + "  ", end=' ')
			else:
				print(str(matrix[i][j]) + " ", end=' ')
		print()
	print()


# rotate matrix 90 degrees
def rotate_matrix90(matrix):

	level = 0
	matrix_size = N  # size of matrix
	last = matrix_size - 1  # very last column, ex: in a 4x4 matrix the last col is 4
	tot_levels = matrix_size/2  # each matrix has a certain number of levels or layers
	
	while level < tot_levels:
		for i in range(level,last):
			swap(level, i, i, last)
			swap(level, i, last, last-i + level)
			swap(level, i, last-i + level, level)

		last -= 1
		level += 1
	
	return matrix


N = int(input("What size would you like the matrix to be: "))

matrix = initialize_matrix(N)
print("----------Original Matrix----------")
display_matrix(matrix)
rotate_matrix90(matrix)
print("----------Rotated Matrix----------")
display_matrix(matrix)
