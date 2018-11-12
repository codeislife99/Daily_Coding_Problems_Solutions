/*
This problem was asked by Oracle.

Given a binary search tree, find the floor and ceiling of a given integer. The floor is the highest element in the tree less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None

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

struct Node{
	int val;
	Node* left;
	Node* right;
	Node(int x):val(x),left(NULL),right(NULL){}
};

pair<int,int> solve(Node* node, float value, int floor= INT_MAX,int ceiling = -INT_MAX){
	if(node==NULL){
		return {floor,ceiling};
	}
	if(node->val == value){
		return {value,value};
	}
	if(node->val > value){
		return solve(node->left, value, floor,node->val);
	}
	else{
		return solve(node->right, value, node->val, ceiling);
	}
	
}

int main(){
	Node* root = new Node(10);
	
	root->left = new Node(5);
	root->right = new Node(15);
	
	root->left->left = new Node(2);
	root->left->right = new Node(8);
	root->right->left = new Node(13);
	root->right->right = new Node(18);

	//[None, None, 6,9,12,14,None,None];
	root->left->right->left = new Node(6);
	root->left->right->right = new Node(9);
	root->right->left->left = new Node(12);
	root->right->left->right = new Node(14);

	root->left->right->left->right = new Node(7);

	float value = 6.1;
	pair<int,int> ans = solve(root,value);
	cout<<"Floor = "<<ans.first<<" Ceiling = "<<ans.second<<"\n";	
}