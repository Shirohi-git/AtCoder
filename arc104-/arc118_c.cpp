#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repi(i, a, b) for (ll i = ll(a); i < ll(b); i++)

int main() {
    ll n;
    cin >> n;

    vector<bool> flag(10001, 0);
    flag[6] = 1, flag[10] = 1, flag[15] = 1;
    ll cnt = 3;

    repi(i, 1, 10001) {
        if (cnt == n) break;
        if ((i % 6 == 0 || i % 10 == 0 || i % 15 == 0) && (flag[i] == 0)) {
            flag[i] = 1, cnt++;
        }
    }
    rep(i, 10001) if (flag[i]) cout << i << ' ';
    cout << endl;
    return 0;
}
