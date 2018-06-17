'''
This problem was asked by Facebook.

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
'''
import math

def helper(a,n,dp):

	if n == 0:
		dp[a][n] = 0
		return dp[a][n]
	elif dp[a][n] >= 0:
		return dp[a][n]
	elif n < (a+1)**2:
		dp[a][n] = helper(a-1,n,dp)
		return dp[a][n];
	else:
		if a!=0:
			dp[a][n] = min(helper(a-1,n,dp),helper(a,n-(a+1)**2,dp)+1)
		else:
			dp[a][n] = n
		return dp[a][n]

def solve(n):
	N = int(math.sqrt(n))
	M = n+1
	dp = [[-1] * M] * N
	return helper(N-1,M-1,dp)

if __name__=='__main__':
	N = [13,27,103,3,15]
	for n in N:
		print(solve(n))
