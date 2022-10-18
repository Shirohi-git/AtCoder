#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define reprs(i, a, b, s) for (ll i = ll(a); i < ll(b); i += (s))

ll N;

int main() {
    cin >> N;
    ll ans = 0;
    reprs(i, 111, 1000, 111) if (i >= N) {
        ans = i;
        break;
    }
    cout << ans << '\n';

    return 0;
}
