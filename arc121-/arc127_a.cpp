#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll N;
const ll T = 10;

ll f_pow(ll x, ll y) {
    ll res = 1;
    while (y > 0) {
        if (y & 1) res *= x;
        x *= x, y >>= 1;
    }
    return res;
}

int main() {
    cin >> N;

    ll ans = 0;
    ll num = 1, cnt = 1;
    while (num <= N) {
        ans += cnt;
        ll sft = 1;
        while (num * f_pow(T,sft) <= N) {
            ll now = num * f_pow(T, sft);
            rep(i, 10) {
                ll tmp = now + i * f_pow(T, sft - 1);
                if (i == 1) continue;
                if (tmp > N) break;
                if (tmp + f_pow(T, sft - 1) > N)
                    ans += cnt * (N % tmp + 1);
                else
                    ans += cnt * f_pow(T, sft - 1);
            }
            sft += 1;
        }
        num = num * 10 + 1, cnt += 1;
    }

    cout << ans << '\n';
    return 0;
}
