#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define all(v) v.begin(), v.end()
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

class Strongly_Conected_Component {
   private:
    ll n;
    vector<ll> flag_dfs, flag_rdfs;

   public:
    ll cnt = 0;
    vector<ll> order, idx;
    matll nm_near, rv_near;

    Strongly_Conected_Component(ll n0, matll near0) {
        n = n0;
        nm_near = near0;
        rv_near = matll(n, vector<ll>(0));
        rep(i, n) for_itr(j, near0[i]) rv_near[j].push_back(i);

        flag_dfs = vector<ll>(n, 0), order = vector<ll>(0);
        rep(i, n) if (!flag_dfs[i]) dfs(i);

        reverse(all(order));
        flag_rdfs = vector<ll>(n, 0), idx = vector<ll>(n, -1);
        for_itr(i, order) if (!flag_rdfs[i]) rdfs(i, cnt), cnt++;
    }

    void dfs(ll v) {
        flag_dfs[v] = 1;
        vector<ll> stack = {v};

        while (!stack.empty()) {
            ll now = stack.back();
            if (nm_near[now].empty()) {
                stack.pop_back();
                order.push_back(now);
            }
            while (!nm_near[now].empty()) {
                ll nxt = nm_near[now].back();
                nm_near[now].pop_back();
                if (!flag_dfs[nxt]) {
                    flag_dfs[nxt] = 1;
                    stack.push_back(nxt);
                    break;
                }
            }
        }
        return;
    }

    void rdfs(ll v, ll c) {
        idx[v] = c;
        vector<ll> stack = {v};

        while (!stack.empty()) {
            ll now = stack.back();
            stack.pop_back();
            if (flag_rdfs[now]) continue;
            flag_rdfs[now] = 1;
            for_itr(nxt, rv_near[now]) if (!flag_rdfs[nxt]) {
                idx[nxt] = c;
                stack.push_back(nxt);
            }
        }
        return;
    }
};

int main() {
    ll n, m;
    cin >> n >> m;
    matll ab(m, vector<ll>(2, 0));
    rep(i, m) cin >> ab[i][0] >> ab[i][1];

    matll near(n, vector<ll>(0));
    for_itr(id, ab) {
        near[id[0] - 1].push_back(id[1] - 1);
    }

    Strongly_Conected_Component scc(n, near);
    vector<ll> cnt(scc.cnt, 0);
    for_itr(id, scc.idx) cnt[id]++;
    
    ll ans = 0;
    for_itr(ci, cnt) ans += ci * (ci - 1) / 2;
    cout << ans << endl;
    return 0;
}
