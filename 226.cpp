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

// void print_graph(unordered_map<char,vector<char>> graph){
// 	for(auto it=graph.begin();it!=graph.end();it++){
// 		cout<<it->first<<":";
// 		for(char vertex:graph[it->first]){
// 			cout<<vertex<<",";
// 		}
// 		cout<<endl;
// 	}
// }

unordered_map<char,vector<char>> create_graph(vector<string>& words){
	unordered_map<char,vector<char>> graph;

	for(auto word:words){
		for(char c:word){
			if(!graph.count(c)){
				graph[c] = {};
			}
		}
	}
	
	for(int i=0;i<words.size()-1;i++){
		for(int j=0;j<words[i].size();j++){
			if(words[i][j] != words[i+1][j]){
				graph[words[i][j]].push_back(words[i+1][j]);
				break;
			}
		}
	}
	// print_graph(graph);
	return graph;

}

void dfs(char vertex, unordered_map<char,vector<char>>& graph, unordered_set<char>& visited,stack<char>& order){
	for(auto nbr:graph[vertex]){
		if(visited.find(nbr)==visited.end()){
			visited.insert(nbr);
			dfs(nbr,graph,visited,order);
		}
	}
	order.push(vertex);
}
vector<char> toposort(unordered_map<char,vector<char>>& graph){
	unordered_set<char> visited;
	stack<char> order;
	for(auto vertex_edge_pair:graph){
		char vertex = vertex_edge_pair.first;
		if(visited.find(vertex)==visited.end()){
			visited.insert(vertex);
 			dfs(vertex,graph,visited,order);
		}

	}
	vector<char> topo_order;
	while(order.size()){
		topo_order.push_back(order.top());
		order.pop();
	}
	return topo_order;
}

int main(){
	// cout<<"Hello World";
	vector<string> words{"xww","wxyz","wxyw","ywx","ywz"};
	unordered_map<char,vector<char>> graph = create_graph(words);
	vector<char> sorted = toposort(graph);
	cout<<sorted.size();
	for(auto c:sorted){
		cout<<c;
	}
	// assert(execution(n,k)==execution2(n,k));
	return 0;
}
