#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)

ll N, L = 1001;
matll PAPER;

int main() {
    cin >> N;
    PAPER = matll(N, vecll(4, -1));
    rep(i, N) rep(j, 4) cin >> PAPER[i][j];

    matll imos(L, vecll(L, 0));
    repitr(pi, PAPER) {
        imos[pi[0]][pi[1]]++, imos[pi[2]][pi[3]]++;
        imos[pi[0]][pi[3]]--, imos[pi[2]][pi[1]]--;
    }
    repr(i, 1, L) rep(j, L) imos[i][j] += imos[i - 1][j];
    rep(i, L) repr(j, 1, L) imos[i][j] += imos[i][j - 1];

    vecll ans(N + 1, 0);
    repitr(xi, imos) repitr(xij, xi) ans[xij]++;
    rep(i, N) cout << ans[i + 1] << '\n';

    return 0;
}
