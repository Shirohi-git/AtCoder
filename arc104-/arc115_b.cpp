#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < int(n); i++)
#define repi(a, b, i) for (int i = int(a); i < int(b); ++i)
#define min(v) *min_element(v.begin(), v.end())

int main() {
    ll n;
    cin >> n;
    vector<vector<ll>> c(n, vector<ll>(n));
    rep(i, n) { rep(j, n) cin >> c[i][j]; }

    ll tmp;
    vector<ll> a(n), b(n);
    tmp = min(c[0]);
    rep(i, n) b[i] = c[0][i] - tmp;
    rep(i, n) a[i] = c[i][0] - b[0];
    rep(i, n) {
        rep(j, n) {
            if (c[i][j] != a[i] + b[j]) {
                cout << "No" << endl;
                return 0;
            }
        }
    }
    cout << "Yes" << endl;
    rep(i, n) cout << a[i] << " ";
    cout << endl;
    rep(i, n) cout << b[i] << " ";
    return 0;
}
