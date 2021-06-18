#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using vectu = vector<tuple<ll, ll>>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll N;
matll AB, NEAR, ITER;

vecll dfs(ll n0, ll s0) {
    vecll flag(n0, 0), cnt(n0 - 1, 0LL);
    flag[s0] = 1;
    vectu stack = {make_tuple(s0, -1)};

    while (!stack.empty()) {
        ll q, edge;
        tie(q, edge) = stack.back();

        bool pop = 1;
        while (!ITER[q].empty()) {
            ll idx = ITER[q].back();
            ITER[q].pop_back();
            ll i = AB[idx][0] - 1;
            if (q == i) i = AB[idx][1] - 1;
            if (flag[i] == 0) {
                pop = 0, flag[i] = 1;
                stack.push_back(make_tuple(i, idx));
                break;
            }
        }
        if (pop) {
            stack.pop_back();
            if (edge > -1) {
                repitr(idx, NEAR[q]) if(idx != edge) cnt[edge] += cnt[idx];
                cnt[edge]++;
            }
        }
    }
    return cnt;
}

int main() {
    cin >> N;
    AB = matll(N, vecll(2));
    rep(i, N - 1) rep(j, 2) cin >> AB[i][j];

    NEAR = matll(N, vecll(0));
    rep(i, N - 1) {
        NEAR[AB[i][0] - 1].push_back(i);
        NEAR[AB[i][1] - 1].push_back(i);
    }
    ITER = NEAR;

    vecll cnt = dfs(N, 0);
    ll ans = 0;
    repitr(ci, cnt) ans += (N - ci) * ci;
    cout << ans << endl;
    return 0;
}
