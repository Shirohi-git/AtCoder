#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define reprs(i, a, b, s) for (ll i = ll(a); i < ll(b); i += s)

int main() {
    ll n, k;
    cin >> n >> k;

    vecll cnt(n + 1, 0);
    repr(i, 2, n + 1) {
        if (cnt[i] > 0) continue;
        reprs(j, i, n + 1, i) cnt[j]++;
    }
    ll ans = 0;
    repitr(ci, cnt) if (ci >= k) ans++;
    cout << ans << endl;
    return 0;
}
