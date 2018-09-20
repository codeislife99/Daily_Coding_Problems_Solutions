#include<set>
#include<unordered_set>
#include<iostream>
#include<utility>
#include<algorithm>    
#include<vector>
using namespace std;

int main(){
	// vector<int> v{1,2,3};
	// for(auto ele:v){
	// 	cout<<ele<<" ";
	// }


	vector<vector<vector<int>>> v(5, vector<vector<int>>(4,vector<int>(3,0)));

	for(int i=0;i<5;i++){
		for(int j=0;j<4;j++){
			for(int k=0;k<3;k++){
			cout<<v[i][j][k]<<" ";
			}
		}
	}

}