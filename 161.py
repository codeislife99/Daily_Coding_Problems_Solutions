'''
This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111 0000 1111.
'''

def solve(num):
 
	# convert number into binary representation
	# output will be like bin(10) = '0b10101'
	binary = bin(num)

	# skip first two characters of binary
	# representation string and reverse
	# remaining string and then append zeros
	# after it. binary[-1:1:-1]  --> start
	# from last character and reverse it until
	# second last character from left
	reverse = binary[-1:1:-1]
	# reverse = (32 - len(reverse))*'0' + reverse
	reverse = '0b' + reverse

	# converts reversed binary string into integer

	return int(reverse,2) 
if __name__ == "__main__":
    num = 12
    print(solve(num))