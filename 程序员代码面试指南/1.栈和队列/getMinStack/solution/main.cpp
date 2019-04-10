#include <iostream>
#include <vector>

#include "stack_min.h"

using namespace std;


int main()
{
    cout << "Test StackMin" << endl;

    StackMin sm;
    sm.push(3);
    sm.push(4);
    sm.push(2);
    sm.push(3);
    sm.push(1);
    sm.debugShow();
    cout<<"Min:"<<sm.getMin()<<endl;
    sm.pop();
    sm.pop();
    sm.debugShow();
    cout<<"Min:"<<sm.getMin()<<endl;

    return 0;
}
