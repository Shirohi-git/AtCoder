#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;

ll N;

int main() {
    cin >> N;

    ll n = N, s = 0;
    while (n) s += n % 10, n /= 10;

    str ans = "No";
    if (N % s == 0) ans = "Yes";
    cout << ans << '\n';
    return 0;
}
