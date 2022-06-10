#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll N, M;
vecll K;
matll A;

int main() {
    cin >> N >> M;
    K = vecll(N), A = matll(N);
    rep(i, N) {
        cin >> K[i];
        A[i] = vecll(K[i]);
        rep(j, K[i]) cin >> A[i][j];
    }
    vecll cnt_a = vecll(M);
    repitr(ai, A) repitr(aij, ai) cnt_a[aij - 1]++;
    ll ans = 0;
    repitr(ci, cnt_a) if (ci == N) ans++;
    cout << ans << '\n';
    return 0;
}
