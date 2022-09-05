#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll N, L, R;

int main() {
    cin >> N >> L >> R;

    ll rht = 0, ans = 0;
    while ((N >> rht) > 0) {
        if ((N >> rht) & 1) {
            ll l = max(1LL << rht, L);
            ll r = min(1LL << (rht + 1), R + 1);
            ans += max(r - l, 0LL);
        }
        rht += 1;
    }
    cout << ans << '\n';
    return 0;
}
