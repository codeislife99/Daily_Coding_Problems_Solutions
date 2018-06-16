'''
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome.
'''

def solve(string):
	S = set()
	for char in string:
		if char in S:
			S.remove(char)
		else:
			S.add(char)
	return len(S)==len(string)%2

if __name__=='__main__':
	strings = ['racecar','daily']
	for string in strings:
		print(solve(string))
