#include<set>
#include<unordered_set>
#include<iostream>
#include<utility>
#include<algorithm>    
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<cmath>
#include<numeric>
#include<cstdlib>
#include<sstream>
#include<functional>

using namespace std;

bool compare(int a ,int b){
	return b<a;
}
int main(){
	queue<int> q;
	q.push(1);q.push(2);q.push(3);q.push(4);q.push(5);q.push(6);
	while(q.size()){
		cout<<q.front()<<" "<<q.back()<<" "<<endl;
		q.pop();
	}

	cout<<double(rand())/RAND_MAX<<endl;
	// Default Priority Queue Ordered From Largest to Smallest
	
	priority_queue<int> pq{1,5};
	pq.push(10);pq.push(20);pq.push(30);pq.push(40);
	// pq.push_back(50);
	while(pq.size()){
		cout << pq.top()<<endl;
		pq.pop();
	}

	// Custom Comparator Priority Queue 

	priority_queue<int,vector<int>,function<bool(int,int)>> pqc(compare);
	pqc.push(10);pqc.push(20);pqc.push(30);pqc.push(40);
	// pq.push_back(50);
	while(pqc.size()){
		cout << pqc.top()<<endl;
		pqc.pop();
	}

	// Deque 
	deque<int> dq{1,2,3,4};
	dq.push_back(5);dq.push_back(6);dq.push_back(7);
	dq.push_front(-1);dq.push_front(-2);dq.push_front(-3);
	while(dq.size()){
		// Popping from the front
		cout<<dq.front()<<endl;
		dq.pop_front(); 

		// Popping from the back
		//cout<<dq.back()<<endl;
		// dq.pop_back();
	}

}