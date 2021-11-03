#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < ll(n); i++)

string O, E;

int main() {
    cin >> O >> E;
    string ans = "";
    rep(i, O.size() + E.size()) {
        if (i % 2 == 0)
            ans += O[i / 2];
        else if (i % 2 == 1)
            ans += E[i / 2];
    }
    cout << ans << '\n';

    return 0;
}
