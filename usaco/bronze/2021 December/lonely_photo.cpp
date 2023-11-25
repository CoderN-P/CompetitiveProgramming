//
// Created by Neel on 11/16/23.
//

#include <iostream>
#define MAX 500000
using namespace std;


long long int solve(int n, char *string){
    int lonely = 0;
    int g[MAX] = { 0 };
    int h[MAX] = { 0 };

    for (int i = 1; i <= n; i++){
        if (string[i-1] == 'H'){
            h[i] = h[i-1] + 1;
            g[i] = g[i-1];
        } else {
            g[i] = g[i-1] + 1;
            h[i] = h[i-1];
        }
    }


    for (int e = n - 1; e > 1; e--){
        for (int start = 0; start < e - 1; start++){
            if (h[e+1]-h[start] == 1 || g[e+1]-g[start] == 1){
                lonely++;
            }
        }
    }

    return lonely;
}

int main(){
    int n;
    char string[MAX];
    cin >> n;
    cin >> string;
    long long int result = solve(n, string);
    cout << result;
    return 0;
}
