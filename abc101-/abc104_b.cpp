#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;

#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)

str S;

int main() {
    cin >> S;
    str ans = "AC";

    if (S[0] != 'A') ans = "WA";
    ll cnt = 0;
    repr(i, 1, S.size()) {
        if (S[i] == 'C' && 1 < i && i < ll(S.size() - 1))
            cnt++;
        else if (isupper(S[i]))
            ans = "WA";
    }
    if (cnt != 1) ans = "WA";

    cout << ans << '\n';
    return 0;
}
