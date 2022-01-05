#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define sort_all(v) sort(v.begin(), v.end())
#define sum(v) accumulate(v.begin(), v.end(), 0LL)

ll N;
matll AB;

int main() {
    cin >> N;
    AB = matll(N, vecll(2));
    rep(i, N) cin >> AB[i][0] >> AB[i][1];
    sort_all(AB);
    ll ans = sum(AB[N - 1]);
    cout << ans << '\n';

    return 0;
}
