#include <bits/stdc++.h>
using namespace std;

string N;

int main() {
    cin >> N;
    while (N.length() < 4) {
        N = '0' + N;
    }
    cout << N << '\n';

    return 0;
}
