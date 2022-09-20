#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define for_itr(id, itr) for (auto& id : itr)

const ll MOD1 = 1e9 + 7;

int main() {
    ll n;
    cin >> n;
    string s, a = "atcoder";
    cin >> s;
    map<char, ll> dic;
    rep(i, 7) dic[a[i]] = i + 1;

    vector<ll> cnt(8, 0);
    for_itr(si, s) {
        if (si == 'a') cnt[1]++;
        if (dic.count(si)) {
            cnt[dic[si]] += cnt[dic[si] - 1];
            cnt[dic[si]] %= MOD1;
        }
    }
    cout << cnt[7] << '\n';
    return 0;
}
