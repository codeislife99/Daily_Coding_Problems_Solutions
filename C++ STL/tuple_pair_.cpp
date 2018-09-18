#include<set>
#include<unordered_set>
#include<iostream>
#include<utility>
#include<algorithm>    
#include<vector>

using namespace std;

int main(){
	tuple<int,char,string> t;
	t = make_tuple(5,'a',"abc");
	cout<<get<0>(t)<<" "<<get<1>(t)<<" "<<get<2>(t)<<endl;

	pair<int,char> f{1,'c'};
	cout<<f.first<<" "<<f.second<<endl;
	return 0;
}