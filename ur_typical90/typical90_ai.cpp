#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define all(v) v.begin(), v.end()

ll N, Q;
vecll Idx, Dist;
matll AB, V;

tuple<vecll, vecll> dfs(const ll& s0, const ll& n0, matll& near0) {
    vecll idx(n0, -1), dist(n0, -1), flag(n0, -1);
    flag[s0] = 0, dist[s0] = 0;
    vecll stack = {s0};

    ll id = 0;
    while (!stack.empty()) {
        ll q = stack.back();
        bool pop = 1;
        while (!near0[q].empty()) {
            ll i = near0[q].back();
            near0[q].pop_back();
            if (flag[i] == -1) {
                flag[i] = flag[q] + 1;
                stack.push_back(i);
                pop = 0;
                break;
            }
        }
        if (pop) {
            stack.pop_back();
            idx[q] = id, dist[id] = flag[q];
            id++;
        }
    }
    return make_tuple(idx, dist);
}

class SparseTable {
   private:
    ll num;

    ll bit_length(ll x) {
        ll cnt = 0;
        while (x) cnt++, x >>= 1;
        return cnt;
    }

    ll stfunc(ll x, ll y) { return min(x, y); }

   public:
    ll n;
    matll table;

    SparseTable(vecll vec0) {
        n = vec0.size();
        num = bit_length(n);
        table = matll(num, vecll(n, -1));
        table[0] = vec0;
        repr(i, 1, num) {
            ll pow2 = (1 << (i - 1));
            vecll& bfo = table[i - 1];
            rep(j, n - (1 << i) + 1) {
                table[i][j] = stfunc(bfo[j], bfo[j + pow2]);
            }
        }
    }

    ll query(ll l, ll r) {
        ll i = bit_length(r - l) - 1;
        return stfunc(table[i][l], table[i][r - (1 << i)]);
    }
};

int main() {
    cin >> N;
    AB = matll(N - 1, vecll(2, 0));
    rep(i, N - 1) cin >> AB[i][0] >> AB[i][1];
    cin >> Q;
    V = matll(Q);
    rep(i, Q) {
        ll k;
        cin >> k;
        V[i] = vecll(k, 0);
        rep(j, k) cin >> V[i][j];
    }

    matll near(N, vecll(0));
    repitr(id, AB) {
        near[id[0] - 1].push_back(id[1] - 1);
        near[id[1] - 1].push_back(id[0] - 1);
    }
    tie(Idx, Dist) = dfs(0, N, near);
    SparseTable ST(Dist);

    rep(i, Q) {
        vecll que;
        repitr(vij, V[i]) que.push_back(Idx[vij - 1]);
        sort(all(que)), reverse(all(que));

        ll p = que.back();
        ll edge = 0;
        while (ll(que.size()) > 1) {
            ll q = que.back();
            que.pop_back();
            ll d_lca = ST.query(q, que.back()) - 1;
            edge += Dist[q] + Dist[que.back()] - 2 * d_lca;
        }
        ll d_pq = ST.query(p, que.back()) - 1;
        edge += Dist[p] + Dist[que.back()] - 2 * d_pq;
        cout << edge / 2 << '\n';
    }

    return 0;
}
