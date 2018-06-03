'''
This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0, 0), (3, 1)]
'''
from heapq import *
import math

def solve(points,central,k):
	if len(points)<=k:
		return points
	pq = []
	for point in points:
		neg_distance = neg_dist(point,central)
		if len(pq)<k:
			heappush(pq,(neg_distance,point))
		elif pq[0][0]<neg_distance:
			heapreplace(pq,(neg_distance,point))

	return [ele[1] for ele in pq]


def neg_dist(a,b):
	return -((a[0]-b[0])**2 + (a[1]-b[1])**2)


if __name__ =='__main__':
	points  = [(0,0),(5,4),(3,1)]
	central = (1,2)
	k = 2
	print(solve(points,central,k))