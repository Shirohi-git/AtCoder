#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll H, W;

int main() {
    cin >> H >> W;
    ll ans = H * W / 2;
    if (H % 2 == 1 && W % 2 == 1) ans += 1;
    if (H == 1 || W == 1) ans = 1;

    cout << ans << '\n';
    return 0;
}
