#include<set>
#include<unordered_set>
#include<iostream>
#include<utility>
#include<algorithm>    
#include<vector>
#include<queue>
#include<deque>
#include<stack>

using namespace std;

int main(){
	queue<int> q;
	q.push(1);q.push(2);q.push(3);q.push(4);q.push(5);q.push(6);
	while(q.size()){
		cout<<q.front()<<" "<<q.back()<<" "<<endl;
		q.pop();
	}

	cout<<double(rand())/RAND_MAX<<endl;
}