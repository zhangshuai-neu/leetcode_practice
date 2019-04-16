#include <iostream>
#include <vector>
#include <string>
#include <sstream>  // stringstream
#include <algorithm>

using namespace std;


class Solution {
public:
    void vectorStringShow(vector<string> &vs){
        for(vector<string>::iterator i=vs.begin(); i!=vs.end(); i++)
            cout<<*i<<" ";
        cout<<endl;
    }

    // 比较 a*b 和 b*a 的大小关系
    // 如果 a*b < b*a ， 则任务s1<s2
    bool lessThan(vector<string>::iterator i, vector<string>::iterator j){
        vector<string>::iterator begin = i;
        vector<string>::iterator end = j;
        if(i>j){
            begin = j;
            end = i;
        }
        
        string sMid; // 中间的部分
        for(vector<string>::iterator iter=begin+1; iter<end; iter++)
            sMid = sMid + *iter;

        return *i+sMid+*j < *j+sMid+*i;
    }

    inline void vectorStringSwap(vector<string>::iterator i, vector<string>::iterator j){
            string tempS = *i;
            *i = *j;
            *j = tempS;
    }

    void sort(vector<string> &vs, vector<string>::iterator begin, vector<string>::iterator end){
        if(begin>=end)
            return;

        /// 获取 partition 的位置
        vector<string>::iterator part = begin;
        for(vector<string>::iterator i=begin; i!=end; i++){
            if( lessThan(i,end) ){
                vectorStringSwap(part,i);
                part++;
            }
        }

        vectorStringSwap(part, end);
        /// 分治
        sort(vs, begin, part-1);
        sort(vs, part+1, end);
    }


    string PrintMinNumber(vector<int> numbers) {
        // 将 numbers 转换成 vector<string>
        stringstream ss;
        vector<string> vs;
        vector<int>::iterator i;
        string * sp = nullptr;
        for(i=numbers.begin(); i!=numbers.end(); i++){
            ss<<*i;
            sp = new string;
            ss>>*sp;
            ss.clear();
            vs.push_back(*sp);
        }

        // 排序
        sort(vs, vs.begin(), vs.end()-1);
        
        // 整理结果
        string retStr;
        for(vector<string>::iterator i=vs.begin(); i!=vs.end(); i++)
            retStr = retStr + *i;
        return retStr;
    }
};


int main(){
    //测试代码
    Solution s;
    vector<int> numbers = {3, 32, 321};
    string str = s.PrintMinNumber(numbers);
    cout<<str<<endl;
    
}
