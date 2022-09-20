#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll h, w;
    cin >> h >> w;

    ll ans = ((h + 1) / 2) * ((w + 1) / 2);
    if (min(h, w) == 1) ans = h * w;
    cout << ans << '\n';
    return 0;
}
