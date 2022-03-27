#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

string A, B;
ll MAX = 1000;

int main() {
    cin >> A >> B;
    ll num = stoll(A + B);

    string ans = "No";
    rep(i, MAX) if (pow(i, 2) == num) ans = "Yes";
    cout << ans << '\n';

    return 0;
}
