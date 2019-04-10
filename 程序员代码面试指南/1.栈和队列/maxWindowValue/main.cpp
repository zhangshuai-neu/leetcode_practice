#include <iostream>
#include <vector>

using namespace std;


class Solution{
public:
    void setInput(vector<int> inData, int inWindow);
    vector<int> getResult();
    void showResult();
    void showQmax();

private:
    int window;
    vector<int> data;
    vector<int> result;
    vector<int> qmax;   /// 中间结果
};

void Solution::setInput(vector<int> inData, int inWindow){
    data = inData;
    window = inWindow;
}

vector<int> Solution::getResult(){
    int i=0;
    int dataSize = data.size();
    for(;i<dataSize;i++){
        if(qmax.empty())
            qmax.push_back(i);
        else{
            /// data[i] > qmax
            /// 如果data[i]大于qmax的末尾，就一直弹出
            while(!qmax.empty() && data[i]>data[qmax.back()]){
                qmax.pop_back();
            }
            qmax.push_back(i);
        }
        /// 处理结果
        if( i-window >= qmax[0]){
            /// 超出window 将头部踢出
            qmax.erase(qmax.begin());
        }
        if(!qmax.empty() && i>1)
            result.push_back(data[qmax[0]]);
        // debug
        // showQmax();
    }
    return result;
}

void Solution::showResult(){
    vector<int>::iterator i = result.begin();
    for(;i!=result.end();i++)
        cout<<*i<<" ";
    cout<<endl;
}

void Solution::showQmax(){
    vector<int>::iterator i =  qmax.begin();
    for(;i!=qmax.end();i++)
        cout<<*i<<" ";
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
