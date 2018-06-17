'''
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B
'''

def solve(arr,loc,color):
	N = len(arr)-1
	M = len(arr[0])-1
	S = set()
	S.add(loc[0]*N + loc[1])
	locs = [loc]
	ori_color = arr[loc[0]][loc[1]]
	diff = [[1,0],[0,1]]
	while len(locs)>0:
		x,y  = locs[0]
		for d in diff:
			a = max(0,x-d[0])
			b = max(0,y-d[1])
			if arr[a][b] == ori_color and ((a*N+b) not in S):
				locs.append([a,b])
				S.add(a*N+b)
			c = min(N,x+d[0])
			d = min(M,y+d[1])
		
			if arr[c][d] == ori_color and ((c*N+d) not in S):
				locs.append([c,d])
				S.add(c*N+d)
		arr[x][y] = color
		locs.pop(0)
	return arr


if __name__ == '__main__':
	arr = [['B', 'B' ,'W'],
		   ['W', 'W' ,'W'],
		   ['W', 'W' ,'W'],
		   ['B', 'B' ,'B']]

	print(solve(arr,(2,2),'G'))