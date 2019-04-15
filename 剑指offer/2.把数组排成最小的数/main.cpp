#include <iostream>
#include <vector>
#include <string>

using namespace std;


class Solution {
public:
    string PrintMinNumber(vector<int> numbers) {
        stringstream ss;
        vector<string> vs;
        vector<int>::iterator i;
        for(i=numbers.begin(); i!=numbers.end(); i++){
            ss<<*i;

            vs.push_back( ss.str() )
        }

    }
};


int main(){
    //测试代码
    Solution s;
    vector<int> numbers = {3，32，321};
    s.PrintMinNumber(numbers);
}
