#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll N, K;

int main() {
    cin >> N >> K;
    ll ans = 0;
    if (N % K > 0) ans++;
    cout << ans << '\n';

    return 0;
}
