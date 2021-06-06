#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

int main() {
    ll n;
    cin >> n;
    vector<string> a(n);
    rep(i, n) cin >> a[i];

    unordered_set<string> dic;
    rep(i, n) if (!dic.count(a[i])) {
        cout << i + 1 << '\n';
        dic.insert(a[i]);
    }
    return 0;
}
