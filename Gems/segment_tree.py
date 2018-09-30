from math import *
class SegmentTree():
	def __init__(self,arr):
		self.arr  = arr
		self.seg_tree = [float('inf') for _ in range(2*(ceil(log(len(arr))/log(2)) ** 2)-1)]
		self.build_tree(0,len(arr)-1,0)
	

	def build_tree(self,low,high,pos):
		if low == high:
			self.seg_tree[pos] = self.arr[low]
			return

		mid = low + (high - low)//2
		self.build_tree(low, mid, 2*pos + 1)
		self.build_tree(mid+1, high, 2*pos + 2)

		self.seg_tree[pos] = min(self.seg_tree[2*pos+1],self.seg_tree[2*pos+2])

	def rmq(self,qlow,qhigh,low,high,pos):
		if qlow<=low and qhigh >= high: # Total Overlap 
			return self.seg_tree[pos]

		if qlow>high or qhigh < low: # No Overlap 
			return float('inf')

		mid = low + (high - low)//2
		return min(self.rmq(qlow,qhigh,low,mid,2*pos+1),
				   self.rmq(qlow,qhigh,mid+1,high,2*pos+2))

	def rminq(self,qlow,qhigh):
		return self.rmq(qlow,qhigh,0,len(self.arr)-1,0)


if __name__ == '__main__':

	arr = [-1,2,4,0] # [-1,-1,0.-1,2,4,0]
	c = SegmentTree(arr)
	print(c.seg_tree)
	print(c.rminq(0,2))
