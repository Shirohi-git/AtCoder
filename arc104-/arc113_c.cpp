#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < int(n); i++)

string s;
ll ans = 0;

int main() {
    cin >> s;
    ll n = s.size();

    vector<ll> cnt(26, 0), tmp(26, 0);
    rep(j, n) {
        ll i = n - 1 - j, idx = s[i] - 'a';
        if (s[i] == s[i + 1] && s[i + 1] != s[i + 2]) {
            ans += n - 1 - i - cnt[idx];
            cnt = tmp;
            cnt[idx] = n - i - 1;
        }
        cnt[idx]++;
    }
    cout << ans << endl;
    return 0;
}
