#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> a(n);
    rep(i, n) cin >> a[i];

    priority_queue<ll> que;
    for_itr(ai, a) que.push(ai);
    rep(i, m) {
        ll tmp = que.top() / 2;
        que.pop();
        que.push(tmp);
    }
    ll ans = 0;
    rep(i, n) {
        ans += que.top();
        que.pop();
    }
    cout << ans << endl;
    return 0;
}
