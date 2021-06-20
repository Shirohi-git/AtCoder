#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

ll N;
const int D = 46;
vecll A, B, C;

int main() {
    cin >> N;
    A = vecll(N), B = vecll(N), C = vecll(N);
    rep(i, N) cin >> A[i];
    rep(i, N) cin >> B[i];
    rep(i, N) cin >> C[i];

    vecll Acnt(D, 0), Bcnt(D, 0), Ccnt(D, 0);
    rep(i, N) Acnt[A[i] % D]++, Bcnt[B[i] % D]++, Ccnt[C[i] % D]++;

    ll ans = 0;
    rep(i, D) rep(j, D) {
        ll k = (D * 2 - i - j) % D;
        ans += Acnt[i] * Bcnt[j] * Ccnt[k];
    }
    cout << ans << '\n';
    return 0;
}
