#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define repi(i, a, b) for (ll i = ll(a); i < ll(b); i++)

int main() {
    ll l, r;
    cin >> l >> r;

    ll ans = 2019, sup = min(r + 1, l + 2020);
    repi(i, l, sup) {
        repi(j, i + 1, sup) {
            ans = min(ans, i * j % 2019);
        }
    }
    cout << ans << endl;
    return 0;
}
