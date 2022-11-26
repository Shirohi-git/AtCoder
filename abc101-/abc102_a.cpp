#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll N;

int main() {
    cin >> N;
    ll ans = N / gcd(N, 2) * 2;
    cout << ans << '\n';
    return 0;
}
