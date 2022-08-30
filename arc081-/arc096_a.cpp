#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B, C, X, Y;

int main() {
    cin >> A >> B >> C >> X >> Y;

    ll ans = A * X + B * Y;
    ans = min(ans, 2 * C * max(X, Y));
    ans = min(ans, 2 * C * Y + A * max(X - Y, 0LL));
    ans = min(ans, 2 * C * X + B * max(Y - X, 0LL));
    cout << ans << '\n';

    return 0;
}
