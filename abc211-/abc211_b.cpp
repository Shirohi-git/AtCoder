#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecs = vector<string>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)

vecs S(4);

void bprint(bool res){
    if (res)
        cout << "No" << endl;
    else
        cout << "Yes" << endl;
    return;
}

int main() {
    rep(i, 4) cin >> S[i];
    bool res = 0;
    rep(i, 4) repr(j, i + 1, 4) res |= (S[i] == S[j]);

    bprint(res);
    return 0;
}
