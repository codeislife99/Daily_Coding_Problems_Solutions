#include<set>
#include<unordered_set>
#include<iostream>
#include<utility>
#include<algorithm>    
#include<vector>
using namespace std;

void printVector(vector<int> v){
	for_each(v.begin(),v.end(),[](int i )
		{
			cout << i << " ";
		});

	cout << endl;
}
int main(){

	vector<int> v = {4,1,3,5,2,3,1,7};
	printVector(v);

	vector<int>:: iterator p = find_if(v.begin(),v.end(), [](int i ){
		return i>4;
	});

	cout << "First Number greater than 4 is : " << *p << endl;

	sort(v.begin(),v.end(),[](const int&a , const int&b) -> bool{
		return a > b;
	});
	
	printVector(v);


	int count_5 = count_if(v.begin(), v.end(), [](int a){
		return a>=5;
	});

	p = unique(v.begin(), v.end(), [](int a,int b){
		return a == b;		
	});

	v.resize(distance(v.begin(),p));
	printVector(v);

	int N = 5;
	
	// int a = 2;
	int count_N = count_if(v.begin(),v.end(), [=](int a){
		return a>=N;
	});

	vector<int> v1 = {3,1,7,9};
	vector<int> v2 = {10,2,7,16,9};

	auto pushinto = [&] (int m){
		v1.push_back(m);
		v2.push_back(m);
	};

	pushinto(20);
	printVector(v1);
	printVector(v2);

	
	char x = '5', y = '1'; 
    (x ^= y), (y ^= x), (x ^= y);  
    cout<<"After Swapping values of x and y are "<<x<<" "<<y;


}