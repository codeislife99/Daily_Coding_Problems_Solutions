#include<set>
#include<unordered_set>
#include<iostream>
#include<utility>
#include<algorithm>    
#include<vector>
using namespace std;

template<class T>
void fun(T a){
	cout << "The main template fun(): " << a << endl;
}

template<>
void fun(int a){
	cout << "Specialized template for int type " << a << endl;
}

template<class T>
class Test{
public:
	Test()
	{
		cout<<"General Template Object \n";
	}
};

template<>
class Test<int>
{
public:
	Test()
	{
		cout << "Specialized template object \n";
	}
};
int main(){
	fun<char>('a');
	fun<int>(5);
	fun<float>(10.1f);
	Test<int> a;
	Test<char> b;
	Test<float> c;
	return 0;
}