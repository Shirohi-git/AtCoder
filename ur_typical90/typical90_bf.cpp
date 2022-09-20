#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define all(v) v.begin(), v.end()

ll N, K, MOD = 100000;

int main() {
    cin >> N >> K;

    vecll flag(MOD, -1);
    ll num = N;
    rep(i, K) {
        if (flag[num] > -1) {
            ll loop = i - flag[num];
            ll idx = flag[num] + (K - i) % loop;
            num = find(all(flag), idx) - flag.begin();
            break;
        }
        flag[num] = i;
        repitr(ni, to_string(num)) num += (ni - '0');
        num %= MOD;
    }
    cout << num << '\n';
    return 0;
}
