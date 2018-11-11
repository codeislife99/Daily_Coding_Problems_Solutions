'''
This problem was asked by Pivotal.

Write an algorithm that finds the total number of set bits in all integers between 1 and N.
'''

def count_set_bits(n):
	return bin(n).count('1')


def solve(n):
	if n == 0:
		return 0

	if n%2==1:
		return (n+1)//2 + 2 * solve(n//2) 

	else:
		return count_set_bits(n) + solve(n-1)

if __name__ == "__main__":
	N = 5
	print(solve(5))

