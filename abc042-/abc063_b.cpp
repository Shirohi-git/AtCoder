#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)

string S;

int main() {
    cin >> S;
    string ans = "yes";

    rep(i, S.size()) repr(j, i + 1, S.size()) if (S[i] == S[j]) ans = "no";
    cout << ans << '\n';
    return 0;
}
