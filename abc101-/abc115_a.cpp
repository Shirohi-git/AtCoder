#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll D;

int main() {
    cin >> D;
    string ans = "Christmas";
    rep(_, 25 - D) ans += " Eve";
    cout << ans << '\n';
    return 0;
}
