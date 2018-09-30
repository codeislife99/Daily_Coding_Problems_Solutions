#include<vector>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <sstream>
#include <ctime>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <sstream>
#include <ctime>
#include <cmath>

using namespace std;

vector<int> GenerateRandVec(int numOfNums, int min, int max);

int main(){
	vector<int> vecVals = GenerateRandVec(10,1, 50);

	for(auto val:vecVals){
		cout << val;
	}
	sort(vecVals.begin(),vecVals.end(),[](int x,int y){return x< y ;});
	// vector<int> evenVecVals;
	// std::copy_if(vecVals.begin(),vecVals.end(), back_inserter(evenVecVals),[](int x){return (x%2) == 0;});


	for(auto val:vecVals){
		cout << val;
	}
	for_each(vecVals.begin(), vecVals.end(), [&](int x){sum += x;});
	cout <<"SUM = "<<sum;

	auto square = [](int i){
		return i*i;
	};

	
}

vector<int> GenerateRandVec(int numOfNums,
        int min, int max){
    std::vector<int> vecValues;
    srand(time(NULL));
    int i = 0, randVal = 0;
    while(i < numOfNums){
        randVal = min + std::rand() % ((max + 1) - min);
        vecValues.push_back(randVal);
        i++;
    }
    return vecValues;
}