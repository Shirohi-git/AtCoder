#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matll = vector<vector<ll>>;

#define sum(v) accumulate(v.begin(), v.end(), ll(0))
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

// 解法1 解説AC O(klog(nm))

//二分探索判定
bool isOK(ll k, ll n, ll m, const vector<ll>& lst, ll mid) {
    ll l = 0, r = 0;
    rep(i, k) {
        l += max(ll(0), (m * lst[i] - mid + n - 1) / n);
        r += (m * lst[i] + mid) / n;
    }
    bool res = (l <= m && m <= r);
    return res;
}

int main() {
    ll k, n, m;
    cin >> k >> n >> m;
    vector<ll> a(k), b(k), r(k);
    rep(i, k) cin >> a[i];

    ll left = -1, right = n * m + 1;
    while (right - left > 1) {
        ll mid = left + (right - left) / 2;
        if (isOK(k, n, m, a, mid))
            right = mid;
        else
            left = mid;
    }

    ll x = right;
    rep(i, k) {
        b[i] = max(ll(0), (m * a[i] - x + n - 1) / n);
        r[i] = (m * a[i] + x) / n;
    }
    ll cnt = sum(b);
    rep(i, k) {
        ll tmp = min(m - cnt, r[i] - b[i]);
        b[i] += tmp, cnt += tmp;
    }
    for_itr(bi, b) cout << bi << ' ';
    cout << endl;
    return 0;
}
