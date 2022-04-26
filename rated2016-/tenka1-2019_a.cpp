#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B, C;

int main() {
    cin >> A >> B >> C;

    string ans = "No";
    if (A < C && C < B) ans = "Yes";
    if (B < C && C < A) ans = "Yes";
    cout << ans << '\n';

    return 0;
}
