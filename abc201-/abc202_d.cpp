#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)

class Combination {
   public:
    matll cnt;
    ll N;

    Combination(ll n0) {
        N = n0;
        cnt = matll(N + 1, vector<ll>(N + 1, 0));

        cnt[0][0] = 1;
        repr(i, 1, N + 1) {
            cnt[i][0] = 1;
            repr(j, 1, N + 1) {
                cnt[i][j] = cnt[i - 1][j - 1];
                cnt[i][j] += cnt[i - 1][j];
            }
        }
    }

    ll count(ll cn, ll cr) { return cnt[cn][cr]; }
};

ll A, B, K;

int main() {
    cin >> A >> B >> K;

    ll cnt = 0, a = A, b = B;
    string ans = "";
    Combination cmb(A + B);
    while (a > 0 && b > 0) {
        ll tmp = cmb.count(a + b - 1, b);
        if (b > 0 && tmp + cnt < K)
            ans += 'b', b -= 1, cnt += tmp;
        else
            ans += 'a', a -= 1;
    }
    ans += string(a, 'a') + string(b, 'b');
    cout << ans << '\n';
    return 0;
}
