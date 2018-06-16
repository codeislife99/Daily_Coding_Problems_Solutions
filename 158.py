'''
This problem was asked by Slack.

You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
'''

def solve(matrix):
	N = len(matrix)
	M = len(matrix[0])
	for i in range(N):
		for j in range(M):
			if i==0 and j==0:
				matrix[i][j] = 1
			elif matrix[i][j] == 1:
				matrix[i][j] = 0
			elif i==0:
				matrix[i][j] = matrix[i][j-1]
			elif j==0:
				matrix[i][j] = matrix[i-1][j]
			else:
				matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
	# print(matrix)
	return matrix[N-1][M-1]

if __name__=='__main__':
	matrix = [[0, 0, 1],
			  [0, 0, 1],
			  [1, 0, 0]]
	print(solve(matrix))
