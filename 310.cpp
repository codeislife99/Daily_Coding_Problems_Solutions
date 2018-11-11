/*
This problem was asked by Pivotal.

Write an algorithm that finds the total number of set bits in all integers between 1 and N.
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


int count_set_bits(int n){
	int count = 0;

	while(n>0){
		count += n&1;
		n >>=1 ;
	}
	return count;
}

int solve(int n){
	if(n == 0){
		return 0;
	}

	if(n%2==1){
		return (n+1)/2 + 2*solve(n/2);
	}

	return count_set_bits(n) + solve(n-1); 
}


int main(){
	int N= 5;
	cout << solve(5) << "\n";

}