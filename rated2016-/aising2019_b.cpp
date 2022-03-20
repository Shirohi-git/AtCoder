#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll N, A, B;
vecll P;

int main() {
    cin >> N >> A >> B;
    P = vecll(N);
    rep(i, N) cin >> P[i];

    ll ans = N, cnt = 0;
    repitr(pi, P) if (pi <= A) cnt += 1;
    ans = min(cnt, ans), cnt = 0;
    repitr(pi, P) if (A < pi && pi <= B) cnt += 1;
    ans = min(cnt, ans), cnt = 0;
    repitr(pi, P) if (B < pi) cnt += 1;
    ans = min(cnt, ans);
    cout << ans << '\n';

    return 0;
}
