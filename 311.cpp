/*
This problem was asked by Sumo Logic.

Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors.
It is guaranteed that the first and last elements are lower than all others

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

int solve(const vector<int>& arr){
	int lo = 0;int hi = arr.size()-1;

	while(lo < hi){
		int mid = lo + (hi - lo)/2;

		if(arr[mid] > arr[mid+1] && arr[mid]> arr[mid-1]){
			return arr[mid];
		}
		if(arr[mid] < arr[mid+1]){
			lo = mid+1;
		}
		else{
			hi = mid-1;
		}
	}
	return arr[lo];
}

int main(){
	vector<int> arr{1,2,3,5,4,2,2,3,4,5,8,1};
	cout << solve(arr)<<"\n";
}