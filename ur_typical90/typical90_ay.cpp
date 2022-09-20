#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define all(v) v.begin(), v.end()

ll N, K, P;
vecll A1, A2;

matll cost_lst(vecll& vec) {
    matll res(N + 1, vecll(0));
    rep(bit, (1 << vec.size())) {
        ll cnt = 0, cost = 0;
        rep(i, vec.size()) if ((bit >> i) & 1) cnt++, cost += vec[i];
        res[cnt].push_back(cost);
    }
    rep(i, N + 1) sort(all(res[i]));
    return res;
}

int main() {
    cin >> N >> K >> P;
    A1 = vecll(N / 2), A2 = vecll(N - N / 2);
    rep(i, N) {
        if (i < N / 2)
            cin >> A1[i];
        else
            cin >> A2[i - N / 2];
    }

    matll lst1 = cost_lst(A1), lst2 = cost_lst(A2);
    ll ans = 0;
    rep(i, N + 1) repitr(y1, lst1[i]) {
        if (K - i >= 0) {
            auto iter = upper_bound(all(lst2[K - i]), P - y1);
            ans += iter - lst2[K - i].begin();
        }
    }
    cout << ans << '\n';
    return 0;
}
