/*
Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

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

struct Node{
	int val;
	Node *next;
	Node(int x):val(x), next(NULL){}
};

void solve(Node* head){
	Node* start = head;
	Node* end = head;

	while(start!= NULL){
		end = start;
		int total = 0;
		bool skip = false;

		while(end!=NULL){
			total += end->val;
			if(total == 0){
				start = end;
				skip = true;
				break;
			}
			end = end->next;

		}
		if(!skip){
			cout<< start->val<<" -> ";
		}
		start = start->next;
	} 
}

int main(){
	Node* head = new Node(3);
	head->next = new Node(4);
	head->next->next = new Node(-7);
	head->next->next->next = new Node(5);
	head->next->next->next->next = new Node(-6);
	head->next->next->next->next->next = new Node(6);
	solve(head);

}


