//
// Created by GreatNeel on 11/18/23.
//
#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    char s[200000];
    cin >> s;
    bool correct[200000];

    for (int i = 0; i < n; i++){
        if (s[i] == 'G'){
            correct[i] = (i%2 == 0);
        } else {
            correct[i] = (i%2 == 1);
        }
    }
    int result = 0;
    for (int i = 1; i < n; i++){
        if (!correct[i] && correct[i-1]){
            result++;
        }
    }
    cout << result;
    return 0;
}