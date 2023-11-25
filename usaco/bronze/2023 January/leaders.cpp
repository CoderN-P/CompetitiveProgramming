//
// Created by Neel on 11/15/23.
//
#include <iostream>

using namespace std;

int solve(int n, char *string, int *e) {
    int farthestH = -1, farthestG = -1;

    for (int i = n-1; i >= 0; i--) {
        if (string[i] == 'H' && farthestH < 0) {
            farthestH = i;
            if (farthestG >= 0) break;
        } else if (string[i] == 'G' && farthestG < 0) {
            farthestG = i;
            if (farthestH >= 0) break;
        }
    }

    int g = -1, h = -1;
    int seenH = false, seenG = false;

    for (int i = 0; i < n; i++){
        if (string[i] == 'H'){
            if (e[i]-1 >= farthestH && !seenH){
                h = i;
            }
            seenH = true;
        } else {
            if (e[i]-1 >= farthestG && !seenG){
                g = i;
            }
            seenG = true;
        }
    }

    int totalG = min(1, g+1)
    int totalH = min(1, h+1);

    for (int i = 0; i < n; i++){
        if (string[i] == 'H' && i != h){
            if (e[i]-1 >= g && i < h){
                totalH++;
            }
        } else if (string[i] == 'G' && i != g){
            if (e[i]-1 >= h && i < h){
                totalG++;
            }
        }
    }

    if (g == -1){
        return totalG;
    } else if (h == -1) {
        return totalH;
    } else {
        return totalG+totalH-1;
    }

}

int main() {
    int n, e[100000];
    char string[100000];
    cin >> n;
    cin >> string;
    for (int i = 0; i < n; i++) {
        cin >> e[i];
    }
    int result = solve(n, string, e);
    cout << result;
    return 0;
}