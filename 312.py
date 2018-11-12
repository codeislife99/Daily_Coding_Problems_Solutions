'''
This problem was asked by Wayfair.

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.

'''

def solve(n,memo = {}):
	if n in memo:
		return memo[n]

	if n < 0:
		memo[n] = 0

	elif n == 0:
		memo[n] = 1

	else:
		memo[n] = solve(n-1,memo) + solve(n-3,memo)

	return memo[n]



if __name__ == '__main__':
	print(solve(10))