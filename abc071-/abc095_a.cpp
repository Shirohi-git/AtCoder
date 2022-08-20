#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define count(v, k) count((v).begin(), (v).end(), (k))

string S;

int main() {
    cin >> S;
    ll ans = 700;
    ans += 100 * count(S, 'o');
    cout << ans << '\n';
    return 0;
}
