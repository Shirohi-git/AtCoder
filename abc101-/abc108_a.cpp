#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll K;

int main() {
    cin >> K;
    ll ans = (K / 2) * ((K + 1) / 2);
    cout << ans << '\n';

    return 0;
}
