# create matrix of size N
def initialize_matrix(N):

	matrix = [[0 for x in range(N)] for y in range(N)]
	counter = 0
	for i in range(N):
		for j in range(N):
			matrix[i][j] = counter
			counter = counter + 1

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


def zero_matrix(matrix, MATRIX_SIZE):

	last = MATRIX_SIZE - 1
	for i in range(N):
		for j in range(N):
			if matrix[i][j] == 0:
				row = i
				col = j

	for x in range(MATRIX_SIZE):
					matrix[row][x] = 0
					matrix[x][col] = 0


N = int(input("What size would you like the matrix to be: "))

matrix = initialize_matrix(N)
print("----------Original Matrix----------")
display_matrix(matrix)

print("----------Zero Matrix----------")
zero_matrix(matrix, N)
display_matrix(matrix)
