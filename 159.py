'''
This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring chracter.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
'''

def solve(string):
	ans = None
	S = set()
	for char in string:
		if char in S:
			return char
		else:
			S.add(char)
	return ans

if __name__=='__main__':
	string = "acbbac"
	print(solve(string))