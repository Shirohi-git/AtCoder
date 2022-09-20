#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll N, Q;
vecll A;
vector<tuple<ll, ll, ll>> Txy;

int main() {
    cin >> N >> Q;
    A = vecll(N);
    rep(i, N) cin >> A[i];
    rep(i, Q) {
        ll t, x, y;
        cin >> t >> x >> y;
        Txy.push_back(make_tuple(t, x, y));
    }

    ll shift = 0;
    repitr(ti, Txy) {
        ll t, x, y;
        tie(t, x, y) = ti;
        ll xs = (x - 1 - shift)%N, ys = (y - 1 - shift)%N;
        xs = (xs + N) % N, ys = (ys + N) % N;
        if (t == 1) swap(A[xs], A[ys]);
        if (t == 2) shift++;
        if (t == 3) cout << A[xs] << '\n';
    }
    return 0;
}
