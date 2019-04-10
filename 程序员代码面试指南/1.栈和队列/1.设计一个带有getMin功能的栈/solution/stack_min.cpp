#include "stack_min.h"

void StackMin::push(int in){
    data.push_back(in);
    // 最小值调整
    if(minStack.empty()){
        minStack.push_back(in);
    } else {
        int minStackEnd = minStack.back();
        int value = minStackEnd<in? minStackEnd:in;
        minStack.push_back(value);
    }
}

int StackMin::pop(void){
    data.pop_back();
    minStack.pop_back();
}

int StackMin::getMin(void){
    return minStack.back();
}

void StackMin::debugShow(void){
    vector<int>::iterator dataIter = data.begin();
    cout<<"data:";
    for(;dataIter!=data.end();dataIter++)
        cout<<*dataIter<<" ";
    cout<<endl;

    vector<int>::iterator msIter = minStack.begin();
    cout<<"minStack:";
    for(;msIter!=minStack.end();msIter++)
        cout<<*msIter<<" ";
    cout<<endl;
}
