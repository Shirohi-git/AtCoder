#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll X, Y;

int main() {
    cin >> X >> Y;

    ll ans = 1, num = X;
    while (num * 2 <= Y) {
        num *= 2;
        ans += 1;
    }
    cout << ans << '\n';
    return 0;
}
