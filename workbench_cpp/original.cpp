#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define min(v) *min_element(v.begin(), v.end())
#define max(v) *max_element(v.begin(), v.end())
#define sort_all(s) sort(s.begin(), s.end())
#define rep(i, n) for (int i = 0; i < int(n); i++)
#define repi(a, b, i) for (int i = int(a); i < int(b); i++)
#define for_itr(id, itr) for (auto&& id : itr)
#define for_dic(key, val, dic) for (auto&& [key, val] : dic)

int main() {
    ll n;
    cin >> n;
    vector<ll> a(n);
    rep(i, n) { cin >> a[i]; }

    return 0;
}
