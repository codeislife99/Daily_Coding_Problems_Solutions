'''
This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
'''

def preprocess(L):
	for i in range(len(L)):
		if i!=0:
			L[i] = L[i]+L[i-1]
	return L

def solve(L,start,end):
	arr = preprocess(L)
	print(arr)
	return (arr[end-1]-arr[max(start-1,0)])

if __name__=='__main__':
	L = [1,2,3,4,5]
	start = 1
	end = 3
	print(solve(L,start,end))