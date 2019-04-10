#include <iostream>
#include <vector>

using namespace std;


class Solution{
public:
    void setInput(vector<int> inData, int inWindow);
    vector<int> getResult();
    void showResult();
    void showQmaxQmin();

private:
    int window;
    vector<int> data;
    vector<int> result;
    vector<int> qmax;   /// 中间结果
    vector<int> qmin;   /// 中间结果
};

void Solution::setInput(vector<int> inData, int inWindow){
    data = inData;
    window = inWindow;
}

vector<int> Solution::getResult(){
    
}

void Solution::showResult(){
    vector<int>::iterator i = result.begin();
    for(;i!=result.end();i++)
        cout<<*i<<" ";
    cout<<endl;
}

void Solution::showQmaxQmin(){
    vector<int>::iterator i =  qmax.begin();
    cout<<"qmax: "
    for(;i!=qmax.end();i++)
        cout<<*i<<" ";
    cout<<endl;

    cout<<"qmin: ";
    for(i=qmin.begin();i!=qmin.end();i++)
        cout<< *i<<" ";
    cout<<endl;
}

///================================
/// 测试代码
///================================
int main()
{
    cout<< " 窗口最大值数组测试： "<< endl;

    Solution s;
    vector<int> inData = {4,3,5,4,3,3,6,7};
    int window = 3;
    s.setInput(inData,window);
    s.getResult();
    s.showResult();

    return 0;
}
