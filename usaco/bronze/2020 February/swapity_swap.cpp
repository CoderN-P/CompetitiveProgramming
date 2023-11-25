#include <iostream>
using namespace std;

int n, k, a1, a2, b1, b2;

int simulate(int idx){

    if (a1 <= idx && idx <= a2) idx = a1+a2 - idx;
    if (b1 <= idx && idx <= b2) idx = b1+b2 - idx;
    return idx;
}


int main(){
    freopen("swap.in", "r", stdin);
    freopen("swap.out", "w", stdout);


    int cows[100];

    cin >> n >> k >> a1 >> a2 >> b1 >> b2;

    for (int i = 1; i <= n; ++i){
        int x = 1;
        int curPos = simulate(i);

        while (curPos != i){
            curPos = simulate(curPos);
            x++;
        }

        for (int j = 0; j < k%x; ++j){
            curPos = simulate(curPos);
        }

        cows[i-1] = curPos;
    }

    for (int i = 0; i < n; i++){
        cout << cows[i] << endl;
    }

    return 0;
}