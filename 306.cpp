/*
This problem was asked by Palantir.

You are given a list of N numbers, in which each number is located at most k places away from its sorted position. For example, if k = 1, a given element at index 4 might end up at indices 3, 4, or 5.

Come up with an algorithm that sorts this list in O(N log k) time.
*/

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

vector<int> solve(const vector<int>& a,int k){
	vector<int> res;
	priority_queue<int> pq;

	for(int i=0;i<k && i<a.size();i++){
		pq.push(-a[i]);
	}
	
	for(int i=k;i<a.size();i++){
		pq.push(-a[i]);
		res.push_back(-pq.top());
		pq.pop();
	}
	while(pq.size()){
		res.push_back(-pq.top());
		pq.pop();
	}	
	return res;
}

int main(){
	vector<int> a{4,3,5};
	int k = 1;
	vector<int> ans = solve(a,k);
	for(auto ele: ans){
		cout << ele << " ";
	}
}