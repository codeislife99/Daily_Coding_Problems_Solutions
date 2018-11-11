'''
This problem was asked by Palantir.

You are given a list of N numbers, in which each number is located at most k places away from its sorted position. For example, if k = 1, a given element at index 4 might end up at indices 3, 4, or 5.

Come up with an algorithm that sorts this list in O(N log k) time.

'''


from heapq import *


def solve(a,k):
	res = []
	heap = []
	for ele in a[:k]:
		heappush(heap,ele)

	for ele in a[k:]:

		heappush(heap,ele)
		res.append(heappop(heap))

	while heap:
		res.append(heappop(heap))

	return res


if __name__ == '__main__':
	a = [4,3,5]
	k = 1
	print(solve(a,k))
	