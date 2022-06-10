#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define sort_all(v) (sort(v.begin(), v.end()))
#define sum(v) (accumulate(v.begin(), v.end(), 0LL))

ll N;
vecll L;

int main() {
    cin >> N;
    L = vecll(N);
    rep(i, N) cin >> L[i];

    sort_all(L);
    ll sum_mx = sum(L) - L[N - 1];

    string ans = "No";
    if (sum_mx > L[N - 1]) ans = "Yes";
    cout << ans << '\n';

    return 0;
}
