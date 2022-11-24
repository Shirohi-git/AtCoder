#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

str S, T;

int main() {
    cin >> S >> T;

    ll n = S.size();
    bool res = 0;
    rep(i, n) {
        bool tmp = 1;
        rep(j, n) tmp &= (S[(i + j) % n] == T[j]);
        res |= tmp;
    }

    str ans = "No";
    if (res == 1) ans = "Yes";

    cout << ans << '\n';
    return 0;
}
