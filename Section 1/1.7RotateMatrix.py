#swap numbers
def swap(i, j, k, l):
	temp = matrix[i][j]
	matrix[i][j] = matrix[k][l]
	matrix[k][l] = temp
# create matrix of size N
def initializeMatrix(N):
	matrix = [[0 for x in range(N)] for y in range(N)]
	counter = 0
	for i in range(N):
		for j in range(N):
			matrix[i][j] = counter
			counter = counter + 1
	return matrix
#display matrix on screen
def displayMatrix(matrix):
	print
	for i in range(N):
		for j in range(N):
			if matrix[i][j] < 10: # added to make matrix look better when numbers are two digits
				print str(matrix[i][j]) + "  ",
			else:
				print str(matrix[i][j]) + " ",
		print
	print

#rotate matrix 90 degrees
def rotateMatrix90(matrix):
	level = 0
	MATRIX_SIZE = N #size of matrix
	last = MATRIX_SIZE - 1 # very last column, ex: in a 4x4 matrix the last col is 4
	totalNumLevels = MATRIX_SIZE/2 # each matrix has a certain number of levels or layers
	
	while(level < totalNumLevels):
		for i in range(level,last):
			swap(level,i,i,last)
			swap(level,i,last,last-i + level)
			swap(level,i,last-i + level,level)
		last = last - 1
		level = level + 1
	
	return matrix

N = int(raw_input("What size would you like the matrix to be: "))

matrix = initializeMatrix(N)
print "----------Original Matrix----------"
displayMatrix(matrix)
rotateMatrix90(matrix)
print "----------Rotated Matrix----------"
displayMatrix(matrix)
