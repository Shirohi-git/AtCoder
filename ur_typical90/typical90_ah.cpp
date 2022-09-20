#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll K, N;
vecll A;

int main() {
    cin >> N >> K;
    A = vecll(N);
    rep(i, N) cin >> A[i];

    ll ans = 0, cnt = 0, l = 0;
    map<ll, ll> dic;
    rep(r, N) {
        if (dic[A[r]] == 0) cnt++;
        dic[A[r]]++;
        while (cnt > K) {
            dic[A[l]]--;
            if (dic[A[l]] == 0) cnt--;
            l++;
        }
        ans = max(ans, r - l + 1);
    }
    cout << ans << endl;
    return 0;
}
