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

def solve(n,f = {},g = {}):
	if n in f and n in g:
		return f[n],g[n]

	if n == 1 or n==2:
		f[n] = n
		g[n] = n

	else:
		f[n] = solve(n-1,f,g)[0] + solve(n-2,f,g)[0] + 2*solve(n-2,f,g)[1]
		g[n] = solve(n-1,f,g)[1] + solve(n-1,f,g)[0]

	return f[n],g[n]

def solve_iter(n):
	f = [0 for _ in range(n+1)]
	g = [0 for _ in range(n+1)]

	f[1] = 1;f[2] = 2;
	g[1] = 1;g[2] = 2;

	for i in range(3,n+1):
		f[i] = f[i-1] + f[i-2] + 2*g[i-2]
		g[i] = g[i-1] + f[i-1]


	return f[n]

if __name__ == '__main__':
	N = 10
	print(solve(N))
	print(solve_iter(N))
	assert(solve(N)[0] == solve_iter(N))
	print(solve_iter(N))


