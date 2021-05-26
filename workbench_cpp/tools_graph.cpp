#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define all(v) v.begin(), v.end()
#define min_itr(v) *min_element(v.begin(), v.end())
#define max_itr(v) *max_element(v.begin(), v.end())
#define sum(v) accumulate(v.begin(), v.end(), 0LL)
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repi(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define for_itr(id, itr) for (auto& id : itr)
#define for_dic(key, val, dic) for (const auto& [key, val] : dic)
#define deg_to_rad(deg) (((deg) / 360) * 2 * M_PI)
#define rad_to_deg(rad) (((rad) / 2 / M_PI) * 360)
#define coutdeci cout << fixed << setprecision(15)

//隣接リスト push_backすると参照壊れるから中身だけコピペ
int nearlist(const matll& lst, matll& near) {
    for_itr(id, lst) {
        near[id[0] - 1].push_back(id[1] - 1);
        near[id[1] - 1].push_back(id[0] - 1);
    }
    return 0;
}

//幅優先探索
int bfs(const int& s, const matll& near, vector<ll>& res) {
    res[s] = 0;
    deque<ll> que;
    que.push_back(s);
    while (!que.empty()) {
        ll q;
        q = que.front();
        que.pop_front();
        for_itr(id, near[q]) {
            if (res[id] > -1) continue;
            res[id] = res[q] + 1;
            que.push_back(id);
        }
    }
    return 0;
}

//ダイクストラ法
int dijkstra(const int& s, const vector<matll>& w_near, vector<ll>& dist) {
    dist[s] = 0;
    priority_queue<vector<ll>> que;
    que.push({0, s});
    while (que.size() > 0) {
        ll d = que.top()[0], q = que.top()[1];
        que.pop();
        if (dist[q] < -d) continue;
        for_itr(nq, w_near[q]) {
            ll nxt = nq[0], tmp = -d + nq[1];
            if (dist[nxt] > tmp) {
                dist[nxt] = tmp;
                que.push({-tmp, nxt});
            }
        }
    }
    return 0;
}

// Unionfind
class Unionfind {
   private:
    vector<ll> res;
    map<ll, vector<ll>> group;

   public:
    ll N;
    vector<ll> parents;

    Unionfind(ll n0) {
        N = n0;
        parents = vector<ll>(N, -1);
    }

    ll find(ll x) {
        if (parents[x] < 0)
            return x;
        else {
            parents[x] = find(parents[x]);
            return parents[x];
        }
    }

    void unite(ll x, ll y) {
        x = find(x), y = find(y);
        if (x == y) return;
        if (parents[x] > parents[y]) {
            ll tmp = x;
            x = y, y = tmp;
        }
        parents[x] += parents[y];
        parents[y] = x;
    }

    bool same(ll x, ll y) { return (find(x) == find(y)); }

    ll roots_cnt() {
        ll cnt = 0;
        for_itr(pi, parents) if (pi < 0) cnt++;
        return cnt;
    }

    vector<ll>& roots() {
        res = vector<ll>(0);
        rep(i, N) if (parents[i] < 0) res.push_back(i);
        return res;
    }

    ll size(ll x) { return -parents[find(x)]; }

    vector<ll>& all_sizes() {
        res = vector<ll>(0);
        for_itr(pi, parents) if (pi < 0) res.push_back(-pi);
        return res;
    }

    vector<ll>& member(ll x) {
        res = vector<ll>(0);
        ll root = find(x);
        rep(i, N) if (find(i) == root) res.push_back(i);
        return res;
    }

    map<ll, vector<ll>>& all_members() {
        group = {};
        rep(i, N) if (parents[i] < 0) group[i] = vector<ll>(0);
        rep(i, N) group[find(i)].push_back(i);
        return group;
    }
};

int main() {
    ll n;
    cin >> n;

    return 0;
}
