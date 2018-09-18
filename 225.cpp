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

using namespace std;
int execution(int n, int k);
int execution2(int n, int k);

int main(){
	cout<<"Hello World";
	int n= 125;int k=2;
	assert(execution(n,k)==execution2(n,k));
	return 0;
}
int execution(int n,int k){
	int last_elim = 1;
	int left = 1;
	int right = n;
	if(k==2){
		int step = 1;
		while(n>=2){
			if(last_elim==1 && n%2==0){
				right -= step;
				last_elim = 1;
				n = n/2;
			}
			else if(last_elim==1 && n%2 != 0){
				last_elim = 0;
				n = n/2 + 1;
			}
			else if(last_elim==0 && n%2!=0){
				last_elim = 1;
				n = n/2;
				left += step;
				right -= step;
			}
			else{//last_elim ==0 && n%2==0
				left += step;
				last_elim = 0;
				n = n/2;

			}
			step *= 2;
		}
	}
	cout<<left<<" "<<right<<endl;
	return left;
}
int execution2(int n,int k){
  if (n == 1)
    return 1;
  else
    /* The position returned by josephus(n - 1, k) is adjusted because the
       recursive call josephus(n - 1, k) considers the original position 
       k%n + 1 as position 1 */
    return (execution2(n - 1, k) + k-1) % n + 1;
}

