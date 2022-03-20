#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll N, H, W;

int main() {
    cin >> N >> H >> W;
    ll ans = (N - H + 1) * (N - W + 1);
    cout << ans << '\n';

    return 0;
}
