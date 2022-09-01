#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : (itr))


ll N;
vecll T;

int main() {
    cin >> N;
    T = vecll(N);
    rep(i, N) cin >> T[i];

    ll ans = 0;
    repitr(ti, T) {
        ll num = (1LL << ti);
        ll cnt = ans / num + 1;
        if (cnt % 2 == 0) cnt += 1;
        ans = cnt * num;
    }
    cout << ans << '\n';
    return 0;
}
