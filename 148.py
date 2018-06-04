'''
	This problem was asked by Apple.

	Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. Gray code is common in hardware so that we don't see temporary spurious values during transitions.

	Given a number of bits n, generate a possible gray code for it.

	For example, for n = 2, one gray code would be [00, 01, 11, 10].
'''
def solve_2(k,s,results):
	if len(s)==k:
		results.append(s)
		return
	for i in range(2):
		string = s+str(i)
		solve_2(k,string,results)

def solve(k):
	results = []
	solve_2(k,'',results)
	return results

if __name__ == '__main__':
	k = 6
	results = solve(k)
	print(results)