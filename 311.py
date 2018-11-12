'''
This problem was asked by Sumo Logic.

Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. 
It is guaranteed that the first and last elements are lower than all others

'''

def solve(arr):
	lo,hi = 0, len(arr) - 1

	while lo < hi:
		mid = lo + (hi - lo)//2

		if arr[mid - 1] < arr[mid] > arr[mid+1]:
			return arr[mid]

		if arr[mid] < arr[mid+1]:
			lo = mid+1

		else:
			hi = mid-1

	return arr[lo]



if __name__ == '__main__':
	arr = [1,2,3,5,4,2,2,3,4,5,8,1]
	print(solve(arr))
	