#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;

ll X, T;

int main() {
    cin >> X >> T;
    ll ans = max(X - T, 0ll);
    cout << ans << '\n';
    return 0;
}
