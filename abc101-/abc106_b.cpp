#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define reprs(i, a, b, s) for (ll i = ll(a); i < ll(b); i += (s))

ll N;

vecll makedivisor(ll num) {
    ll p = 1;
    vecll upper(0), lower(0);
    while (p * p <= num) {
        if (num % p == 0) {
            lower.push_back(p);
            if (p * p != num) upper.push_back(num / p);
        }
        p += 1;
    }
    reverse(upper.begin(), upper.end());
    lower.insert(lower.end(), upper.begin(), upper.end());
    return lower;
}

int main() {
    cin >> N;

    ll ans = 0;
    reprs(i, 1, N + 1, 2) {
        vecll div = makedivisor(i);
        if (div.size() == 8) ans += 1;
    }
    cout << ans << '\n';
    return 0;
}
