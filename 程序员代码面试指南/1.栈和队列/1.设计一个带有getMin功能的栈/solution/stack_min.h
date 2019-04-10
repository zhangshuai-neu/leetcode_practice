#ifndef STACK_MIN
#define STACK_MIN

#include <vector>
#include <iostream>
using namespace std;

class StackMin{
public:
    void push(int in);
    int pop(void);
    int getMin(void);

    // debug function
    void debugShow(void);
private:
    vector<int> data;
    vector<int> minStack;
};

#endif // STACK_MIN
