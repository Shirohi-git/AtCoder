#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll N, P;
vecll A;

int main() {
    cin >> N >> P;
    A = vecll(N);
    rep(i, N) cin >> A[i];

    ll cnt = 0;
    repitr(ai, A) if (ai < P) cnt += 1;
    cout << cnt << '\n';

    return 0;
}
