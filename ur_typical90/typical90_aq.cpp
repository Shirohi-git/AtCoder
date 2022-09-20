#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;
using vecs = vector<string>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define max_val(v) *max_element(v.begin(), v.end())
#define itr_add(v1,v2) v1.insert(v1.end(), v2.begin(), v2.end())


ll H, W, SX, SY, TX, TY;
vector<string> S;

class c_near {
   private:
    const ll hw = H * W;

    vecll nearloop(const ll r1, const ll r2, const bool rev) {
        vecll res(hw, -1);
        rep(j, r1) {
            bool bfo = 1;
            rep(i, r2) {
                ll x = j, y = i;
                if (rev) x = i, y = j;
                if (S[x][y] == '.') {
                    cnt += bfo;
                    res[x * W + y] = cnt;
                }
                bfo = (S[x][y] == '#');
            }
        }
        return res;
    }

   public:
    ll cnt = -1;
    vecll col, row, flag;
    matll idx, dic;

    c_near(void) {
        col = nearloop(W, H, 1), row = nearloop(H, W, 0);
        idx = matll(hw, vecll(2, -1));
        rep(i, hw) idx[i][0] = col[i], idx[i][1] = row[i];

        ll maxidx = max_val(row) + 1;
        flag = vecll(maxidx, 0);
        dic = matll(maxidx, vecll(0));
        rep(i, hw) {
            if (col[i] == -1) continue;
            dic[col[i]].push_back(i);
            dic[row[i]].push_back(i);
        }
    }
};

ll bfs(const ll& s, const ll& g, c_near& near0) {
    vecll dist(H * W, -2);
    dist[s] = -1;

    deque<ll> que;
    que.push_back(s);
    while (!que.empty()) {
        ll q = que.front();
        que.pop_front();

        vecll vec(0);
        repitr(i, near0.idx[q]){
            if (near0.flag[i] == 0){
                itr_add(vec, near0.dic[i]);
                near0.flag[i] = 1;
            }
        }

        repitr(i, vec) {
            if (dist[i] == -2) {
                dist[i] = dist[q] + 1;
                que.push_back(i);
            }
        }
        if (dist[g] > -2) return dist[g];
    }
    return -2;
}

int main() {
    cin >> H >> W >> SX >> SY >> TX >> TY;
    SX--, SY--, TX--, TY--;
    S = vecs(H);
    rep(i, H) cin >> S[i];

    c_near near;
    ll ans = bfs(SX * W + SY, TX * W + TY, near);
    cout << ans << '\n';
    return 0;
}
