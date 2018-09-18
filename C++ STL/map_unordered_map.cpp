#include<set>
#include<unordered_set>
#include<iostream>
#include<utility>
#include<algorithm>    
#include<vector>
using namespace std;

namespace std {
template <> struct hash<pair<int, char>> {
    inline size_t operator()(const pair<int, char> &v) const {
        hash<int> int_hasher;
        hash<char> char_hasher;
        return int_hasher(v.first) ^ char_hasher(v.second);
    }
};
}
int main(){
	set<int> t;
	// Insert 
	t.insert(3);t.insert(4);t.insert(5);t.insert(40);t.insert(20);t.insert(10);
	// Iterate

	// 1. Using auto 
	for(auto ele:t){
		cout <<ele<<" ";
	}
	cout << endl;

	// 2. Using iterator
	// reverse(t.begin(),t.end());

	for(auto itr = t.begin();itr!=t.end();itr++){
		cout << *itr<<" " ;
	}
	cout << endl;
	// Remove 

	t.erase(5);
	for(auto ele:t){
		cout << ele<<" ";
	}
	cout<<endl;

	// Bound Elements;

	cout << *t.lower_bound(9)<<endl;
	cout << *t.upper_bound(20)<<endl;

	//	Find 
	if(t.find(50)!=t.end()){
		cout << "FOUND" <<endl;
	}
	else{
		cout << "NOT FOUND" << endl;
	}

	if(t.find(40)!=t.end()){
		cout << "FOUND"<<endl;
	}
	else{
		cout << "NOT FOUND" <<endl;
	}

	unordered_set<int> t2;
	// Insert 
	t2.insert(3);t2.insert(4);t2.insert(5);t2.insert(40);t2.insert(20);t2.insert(10);
	// Iterate

	// 1. Using auto 
	for(auto ele:t2){
		cout <<ele<<" ";
	}
	cout << endl;

	// 2. Using iterator
	// reverse(t.begin(),t.end());

	for(auto itr = t2.begin();itr!=t2.end();itr++){
		cout << *itr<<" " ;
	}
	cout << endl;
	// Remove 

	t2.erase(5);
	for(auto ele:t2){
		cout << ele<<" ";
	}
	cout<<endl;


	//	Find 
	if(t2.find(50)!=t2.end()){
		cout << "FOUND" <<endl;
	}
	else{
		cout << "NOT FOUND" << endl;
	}

	if(t2.find(40)!=t2.end()){
		cout << "FOUND"<<endl;
	}
	else{
		cout << "NOT FOUND" <<endl;
	}
	return 0;
}