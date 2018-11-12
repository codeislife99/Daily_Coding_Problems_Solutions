class Node():
	def __init__(self,val):
		self.val   = val
		self.left  = None
		self.right = None 

class Solution():

	def solve(self,root, value):
		self.value = value
		self.floor = -float('inf')
		self.ceiling = float('inf')
		self.recur(root)

		return self.floor, self.ceiling

	def recur(self,node):

		if node is None:
			return

		print(node.val)

		if node.val <= self.value and node.val >= self.floor:
			self.floor = node.val
			self.recur(node.right)

		if node.val >= self.value and node.val <= self.ceiling:
			self.ceiling = node.val
			self.recur(node.left)




if __name__ == '__main__':
	# Level 1
	root = Node(10)
	
	# Level 2
	root.left = Node(5)
	root.right = Node(15)
	
	# Level 3
	root.left.left = Node(2)
	root.left.right = Node(8)
	root.right.left = Node(13)
	root.right.right = Node(18)

	# Level 4
	#[None, None, 6,9,12,14,None,None]
	root.left.right.left = Node(6)
	root.left.right.right = Node(9)
	root.right.left.left = Node(12)
	root.right.left.right = Node(14)

	# Level 5
	#[None, 7]
	root.left.right.left.right = Node(7)

	value = 6.1
	s = Solution()
	floor,ceiling = s.solve(root,value)
	print("Floor = ", floor, "Ceiling = ",ceiling)
