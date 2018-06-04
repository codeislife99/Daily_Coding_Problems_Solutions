'''
This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
'''
class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

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

def solve(root):
	if root!=None:
		root.left,is_faulty_left = solve(root.left)
		root.right,is_faulty_right = solve(root.right)
		if root.val == 0 and is_faulty_left and is_faulty_right:
			return None, True
		return root, False
	return None,True


if __name__ == '__main__':
	root = Node(0)
	root.left = Node(1)
	root.right = Node(0)
	root.right.left = Node(1)
	root.right.right = Node(0)
	root.right.left.left = Node(0)
	root.right.left.right = Node(0)
	root, _ = solve(root)
	levelorder(root)
