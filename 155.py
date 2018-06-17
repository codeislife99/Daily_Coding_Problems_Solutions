'''
Given a list of elements, find the majority element, which appears more than half the times (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 1], return 1.
'''


def solve(arr):
	votes = 0
	number = None
	for ele in arr:
		if votes == 0:
			number = ele
			votes+=1
		elif ele!=number:
			votes-=1
		else ele==number:
			votes+=1
	return number

if __name__=='__main__':
	arr = [1, 2, 1, 1, 3, 4, 1]
	print(solve(arr))
