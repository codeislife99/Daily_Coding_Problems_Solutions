'''
This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
'''
import random

def solve(arr,prob_arr):
	prob = random.uniform(0,1)
	cum_prob = 0.0 
	for i,ele in enumerate(prob_arr):
		cum_prob += ele
		if prob <= cum_prob:
			return arr[i]


if __name__ == '__main__':
	arr      = [1,2,3,4]
	prob_arr = [0.1,0.5,0.2,0.2]	
	print(solve(arr,prob_arr))