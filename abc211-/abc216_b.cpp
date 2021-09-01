#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecs = vector<string>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)


ll N;
vector<vecs> ST;

int main() {
    cin >> N;
    ST = vector(N, vecs(2));
    rep(i, N) cin >> ST[i][0] >> ST[i][1];

    rep(i, N) repr(j, i + 1, N) {
        if (ST[i][0] == ST[j][0] && ST[i][1] == ST[j][1]) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;

    return 0;
}
