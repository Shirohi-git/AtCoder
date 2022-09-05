#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B, C;

int main() {
    cin >> A >> B >> C;
    ll ans = 10 * A + B + C;
    ans = max(ans, 10 * B + A + C);
    ans = max(ans, 10 * C + A + B);
    cout << ans << '\n';
    return 0;
}
