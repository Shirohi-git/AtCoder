#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll f_pow(ll x, ll y) {
    ll res = 1;
    while (y > 0) {
        if (y & 1) res = (res * x);
        x = (x * x);
        y >>= 1;
    }
    return res;
}

int main() {
    ll a, b, c;
    cin >> a >> b >> c;

    if (a < f_pow(c, b)) {
        cout << "Yes" << endl;
        return 0;
    }
    cout << "No" << endl;
    return 0;
}
