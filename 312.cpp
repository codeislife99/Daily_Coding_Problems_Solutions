/*
This problem was asked by Wayfair.

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.

*/
#include <climits>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <unordered_map>
#include <unordered_set>

using namespace std;


int solve(int n,unordered_map<int,int>memo = {}){
	if(memo.count(n)){
		return memo[n];
	}
	if(n<0){
		memo[n] = 0;
	}
	else if(n==0){
		memo[n] = 1;
	}
	else{
		memo[n] = solve(n-1,memo) + solve(n-3,memo);
	}
	return memo[n];
}


int main(){
	cout << solve(10) << "\n";
}