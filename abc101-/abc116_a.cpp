#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B, C;

int main() {
    cin >> A >> B >> C;
    ll ans = min(A * B, B * C);
    ans = min(ans, C * A) / 2;
    cout << ans << '\n';
    return 0;
}
