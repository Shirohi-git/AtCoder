#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto &id : itr)
#define max_val(v) (*max_element((v).begin(), (v).end()))
#define min_val(v) (*min_element((v).begin(), (v).end()))

ll N, a, b;
vecll A;

bool isOK(ll num) {
    ll pl = 0, mn = 0;
    repitr(vi, A) {
        if (vi < num) pl += (num - vi + a - 1) / a;
        if (vi > num) mn += (vi - num) / b;
    }
    bool res = true;
    if (pl > mn) res = false;
    return res;
}

ll binary_search(ll l, ll r) {
    ll left = l, right = r + 1;
    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        if (isOK(mid))
            left = mid;
        else
            right = mid;
    }
    return left;
}

int main() {
    cin >> N >> a >> b;
    A = vecll(N);
    rep(i, N) cin >> A[i];

    ll ans = binary_search(min_val(A), max_val(A));
    cout << ans << '\n';
    return 0;
}
