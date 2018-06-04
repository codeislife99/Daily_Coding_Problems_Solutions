'''
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
'''
class Node():
	def __init__(self,val):
		self.next = None
		self.val = val

def traverse(head):
	print("TRAVERSING NEW LIST")
	start = head
	while head!=None:
		print(head.val,end = " ")
		head = head.next
	print("")
	return start
def solve(head,prev = None):
	if head == None or head.next == None:
		return head

	while head!= None and head.next!=None:
		temp = head.next
		head.next = head.next.next
		temp.next = head
		if prev!=None:
			prev.next = temp
			prev = prev.next.next
		else:
			root = temp
			prev = head
		head = prev.next
	return root
if __name__ == '__main__':
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)
	head.next.next.next.next.next = Node(6)
	head.next.next.next.next.next.next = Node(7)

	# head = traverse(head)
	# print(head.val)
	head = solve(head)
	traverse(head)