#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll N;
const ll INF = 2000000;

int main() {
    cin >> N;

    ll num = N;
    map<ll, ll> dic;

    ll ans = INF;
    rep(i, INF) {
        if (dic.find(num) != dic.end()) {
            ans = i+1;
            break;
        }
        dic[num] = i;
        if (num % 2 == 1)
            num = 3 * num + 1;
        else if (num % 2 == 0)
            num /= 2;
    }
    cout << ans << '\n';
    return 0;
}
