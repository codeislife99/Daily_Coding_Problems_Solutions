'''
This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:

push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap
'''

from heapq import *

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		heappush(self.items,(-len(self.items)-1,item))

	def pop(self):
		a = heappop(self.items)
		return a[1]

	def peek(self):
		return self.items[0][1]
	
	def size(self):
		return len(self.items)

if __name__=='__main__':

	S = Stack()
	print(S.isEmpty())
	S.push(23)
	S.push(65)
	print(S.peek())
	print(S.pop())
	S.push(45)
	S.push(32)
	print(S.peek())
	print(S.pop())
	print(S.size())
	print(S.isEmpty())