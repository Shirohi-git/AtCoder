#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define sort_all(s) sort(s.begin(), s.end())
#define rep(i, n) for (int i = 0; i < int(n); i++)
#define for_itr(id, itr) for (auto&& id : itr)
#define for_dic(key, val, dic) for (auto&& [key, val] : dic)

int main() {
    ll n;
    cin >> n;
    vector<string> s(n);
    rep(i, n) { cin >> s[i]; }

    map<string, ll> dict;
    for_itr(si, s) {
        sort_all(si);
        if (dict.count(si))
            dict[si]++;
        else
            dict[si] = 1;
    }
    ll ans = 0;
    for_dic(k, v, dict) ans += v * (v - 1) / 2;
    cout << ans << endl;
    return 0;
}
