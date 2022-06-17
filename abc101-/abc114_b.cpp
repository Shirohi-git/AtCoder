#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll S;

int main() {
    cin >> S;

    ll ans = 1000;
    while (S > 100) {
        ans = min(abs(753 - S % 1000), ans);
        S /= 10;
    }

    cout << ans << '\n';
    return 0;
}
