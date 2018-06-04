class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

def preorder(root):
	if root!= None: 
		print(root.val)
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root!= None:
		postorder(root.left)
		postorder(root.right)
		print(root.val)

def inorder(root):
	if root!= None:
		inorder(root.left)
		print(root.val)
		inorder(root.right)

def levelorder_helper(root,level,level_nodes):
	if root!=None:
		if len(level_nodes) <= level:
			level_nodes.append([root.val])
		else:
			level_nodes[level].append(root.val)
		levelorder_helper(root.left,level+1,level_nodes)
		levelorder_helper(root.right,level+1,level_nodes)


def levelorder(root):
	level_nodes = []
	level = 0
	levelorder_helper(root,level,level_nodes)
	print(level_nodes)


if __name__ == '__main__':
	root = Node(0)
	root.left = Node(1)
	root.right = Node(2)
	root.right.left = Node(3)
	root.right.right = Node(4)
	root.right.left.left = Node(5)
	root.right.left.right = Node(6)

	preorder(root)
	levelorder(root)