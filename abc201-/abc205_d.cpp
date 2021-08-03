#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define all(v) v.begin(), v.end()

ll N, Q;
vecll A, K;

int main() {
    cin >> N >> Q;
    A = vecll(N), K = vecll(Q);
    rep(i, N) cin >> A[i];
    rep(i, Q) cin >> K[i];

    vecll cnt(N);
    rep(i, N) cnt[i] = A[i] - (i + 1);

    repitr(ki, K) {
        ll ans = A[N - 1] + (ki - cnt[N - 1]);
        ll idx = lower_bound(all(cnt), ki) - cnt.begin();
        if (idx < N) ans = A[idx] - (cnt[idx] - ki + 1);
        cout << ans << '\n';
    }

    return 0;
}
