class Node():
	def __init__(self,val):
		self.val   = val
		self.left  = None
		self.right = None 

def solve(node,value,floor = None,ceiling = None):
	if node is None:
		return floor,ceiling

	if node.val == value:
		floor,ceiling = value,value

	elif node.val < value:
		floor,ceiling = solve(node.right, value, node.val, ceiling)

	else:
		floor,ceiling = solve(node.left, value, floor, node.val)

	return floor,ceiling

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

	# s = Solution()
	# floor,ceiling = s.solve(root,value)
	floor,ceiling = solve(root,value)
	print("Floor = ", floor, "Ceiling = ",ceiling)
