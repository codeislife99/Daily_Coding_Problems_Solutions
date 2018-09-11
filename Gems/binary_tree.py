class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

class TreeTraversal(object):
	def __init__(self,root):
		self.root          = root
		self.preorder      = []
		self.postorder     = []
		self.inorder       = []
		self.levelorder    = [] 
		self.preorder_it   = []
		self.postorder_it  = []
		self.inorder_it    = []
		self.levelorder_it = []  

	def preorder_rec(self,root):
		if root!= None: 
			self.preorder.append(root.val)
			self.preorder_rec(root.left)
			self.preorder_rec(root.right)

	def preorder_iter(self,root):
		pass

	def postorder_rec(self,root):
		if root!= None:
			self.postorder_rec(root.left)
			self.postorder_rec(root.right)
			self.postorder.append(root.val)

	def postorder_iter(self,root):
		pass

	def inorder_rec(self,root):
		if root!= None:
			self.inorder_rec(root.left)
			self.inorder.append(root.val)
			self.inorder_rec(root.right)

	def inorder_iter(self,root):
		stack = []
		while root is not None or len(stack) > 0:
			while root!=None:
				stack.append(root)
				root = root.left
			root = stack.pop()
			self.inorder_it.append(root.val)
			root = root.right

	def levelorder_rec(self,root,level):
		if root!=None:
			if len(self.levelorder) <= level:
				self.levelorder.append([root.val])
			else:
				self.levelorder.append(root.val)
			self.levelorder_rec(root.left ,level+1)
			self.levelorder_rec(root.right,level+1)

	def levelorder_iter(self,root,level):
		pass
		
if __name__ == '__main__':
	root = Node(0)
	root.left = Node(1)
	root.right = Node(2)
	root.right.left = Node(3)
	root.right.right = Node(4)
	root.right.left.left = Node(5)
	root.right.left.right = Node(6)


	T = TreeTraversal(root)
	T.inorder_rec(T.root)
	T.inorder_iter(T.root)
	print(T.inorder)
	print(T.inorder_it)