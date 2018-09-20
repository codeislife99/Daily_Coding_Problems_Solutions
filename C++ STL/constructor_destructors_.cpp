#include<set>
#include<unordered_set>
#include<iostream>
#include<utility>
#include<algorithm>    
#include<vector>
using namespace std;

class Point{
private:
	int x;
	int y;
public:

	Point(int a,int b) : x(a), y(b) {}
	Point(){
		x = 0;
		y = 0;
	}

	int getX(){
		return x;
	}

	int getY(){
		return y;
	}

};
int main(){
	Point p(10,20);
	cout<<p.getX()<< " "<<p.getY();
	return 0;
}
