#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B, C, D;

int main() {
    cin >> A >> B >> C >> D;
    ll ans = 0;
    if (A <= C) ans = max(ans, min(B - C, D - C));
    if (C <= A) ans = max(ans, min(D - A, B - A));
    cout << ans << '\n';

    return 0;
}
