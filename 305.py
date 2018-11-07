'''
Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
'''

class Node():
	def __init__(self, val):
		self.next = None
		self.val = val


def solve(head):
    start = end = head

    while start:
        end = start
        total = 0
        skip = False

        while end:
            total += end.val
            if total == 0:
                start = end
                skip = True
                break
            end = end.next

        if not skip:
            print(start.val)

        start = start.next




if __name__ == "__main__":

	head = Node(3)
	head.next = Node(4)
	head.next.next = Node(-7)
	head.next.next.next = Node(5)
	head.next.next.next.next = Node(-6)
	head.next.next.next.next.next = Node(6)
	solve(head)

	# while head:
	# 	print(head.val+" -> ")

