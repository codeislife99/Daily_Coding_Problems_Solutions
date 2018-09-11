class BinarySearch(object):
	def __init__(self,nums):
		self.nums = nums

	def bsearch_lesserequal(self,target):
		low  = 0 
		high = len(self.nums) - 1
		
		if self.nums[low] > target:
			return None,None


		while(low != high):
			mid = low + (high-low)//2
			if(target > self.nums[mid]): # Change this to >= to get greater only 
				low = mid+1
			else:
				high = mid
		return low,self.nums[low]

	def bsearch_greaterequal(self,target):
		low  = 0 
		high = len(self.nums) - 1

		if self.nums[high] < target:
			return None,None

		while(low != high):
			mid = low + (high-low)//2
			if(target >= self.nums[mid]):
				low = mid+1
			else:
				high = mid
		if self.nums[low] == target:
			return low,self.nums[low]
		return low-1,self.nums[low-1]

	def bsearch_equal(self,target):
		index,ele = self.bsearch_greaterequal(target)
		if ele!=target:
			return None,None
		return index,ele

if __name__   == '__main__':
	arr       = [2,2]
	B         = BinarySearch(arr)
	index1,ele1 = B.bsearch_greaterequal(2)
	index2,ele2 = B.bsearch_lesserequal(2)
	index3,ele3 = B.bsearch_equal(2)

	print(index1,ele1)
	print(index2,ele2)
	print(index3,ele3)
