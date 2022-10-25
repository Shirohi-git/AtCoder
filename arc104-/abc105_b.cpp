#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll N;

int main() {
    cin >> N;
    str ans = "No";
    rep(i, N / 7 + 1) if ((N - 7 * i) % 4 == 0) ans = "Yes";
    cout << ans << '\n';
    return 0;
}
