#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B, C;

int main() {
    cin >> A >> B >> C;
    bool res = (A + B == C || B + C == A || C + A == B);
    if (res)
        cout << "Yes" << '\n';
    else
        cout << "No" << '\n';

    return 0;
}
