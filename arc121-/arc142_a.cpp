#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;
#define all(v) (v).begin(), (v).end()

ll N;
str K;

int main() {
    cin >> N >> K;
    ll k = stoll(K);
    reverse(all(K));
    ll k2 = stoll(K);
    reverse(all(K));
    ll k1 = stoll(K);

    ll ans = 0;
    if (k != min(k1, k2))
        ans = 0;
    else {
        if (k1 != k2)
            while (k1 <= N) ans += 1, k1 *= 10;
        while (k2 <= N) ans += 1, k2 *= 10;
    }

    cout << ans << '\n';
    return 0;
}
