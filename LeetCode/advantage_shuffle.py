from heapq import *

def ranking(a):
	q = []
	for i,ele in enumerate(a):
		heappush(q,(ele,i))
	return q

def solve(A,B):
	ranking_B = ranking(B)

	ranking_A = []
	for i,ele in enumerate(A):
		heappush(ranking_A,ele)

	ele_b,index_B = heappop(ranking_B)
	remaining = []
	set_done = set([])
	while len(ranking_A) > 0:
		ele_a = heappop(ranking_A)

		if ele_a <= ele_b:
			remaining.append(ele_a)
			continue
		else:
			# orig = A[index_B]
			A[index_B] = ele_a
			set_done.add(index_B)
			# A[index_A] = orig
			if len(ranking_A) > 0:
				ele_b, index_B = heappop(ranking_B)

	for i in range(len(A)):
		if i in set_done:
			continue
		else:
			A[i] = remaining.pop(0)
			set_done.add(i)
	# print(remaining)
	return A



if __name__ =='__main__':
	# A = [2,7,11,15]
	# B = [1,10,4,11]
	A = [5621,1743,5532,3549,9581]
	B = [913,9787,4121,5039,1481]
	print(solve(A,B))