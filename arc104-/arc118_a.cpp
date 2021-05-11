#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll INF = (1LL << 62) / 100;

//二分探索判定
bool isOK(const ll& tax, const ll& num, ll mid) {
    bool res = (mid * (100 + tax) / 100 - mid >= num);
    return res;
}

//二分探索
ll binary_search(const ll& tax, const ll& num, ll l, ll r) {
    while (r - l > 1) {
        ll mid = l + (r - l) / 2;
        if (isOK(tax, num, mid))
            r = mid;
        else
            l = mid;
    }
    return l;
}

int main() {
    ll t, n;
    cin >> t >> n;

    ll ans = binary_search(t, n, -1LL, INF);
    ans = ans * (100 + t) / 100 + 1;
    cout << ans << endl;
    return 0;
}
