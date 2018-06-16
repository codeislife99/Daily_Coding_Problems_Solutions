'''
This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
'''

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def solve(arr):
	ans_arr = []
	for item in arr:
		ans_arr.append(item)
		if not isinstance(item,int):
			sign = ans_arr.pop()
			b = ans_arr.pop()
			a = ans_arr.pop()
			ans_arr.append(compute(a,b,sign))
	return ans_arr[0]

def compute(a,b,sign):
	if sign=='+':
		return a+b
	elif sign == '-':
		return a-b
	elif sign == '*':
		return a*b
	else:
		return a/b

if __name__=='__main__':
	polish_array = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
	print(solve(polish_array))