#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define all(v) v.begin(), v.end()

ll N, K;
matll AB;

int main() {
    cin >> N >> K;
    AB = matll(N, vecll(2));
    rep(i, N) cin >> AB[i][0] >> AB[i][1];

    vecll point;
    repitr(abi, AB) {
        point.push_back(abi[1]);
        point.push_back(abi[0] - abi[1]);
    }
    sort(all(point)), reverse(all(point));
    ll* s = &point[0];
    ll ans = accumulate(s, s + K, 0LL);
    cout << ans << '\n';
    return 0;
}
