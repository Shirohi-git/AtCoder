#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ll a, b, c;
    cin >> a >> b >> c;

    ll n = gcd(a, gcd(b, c));
    ll ans = (a + b + c) / n - 3;
    cout << ans << endl;

    return 0;
}
