#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

template <typename T>
void coutitr(const T& itr) {
    for (auto& id : itr) cout << id << ' ';
    cout << '\n';
    return;
}

ll N, M;
matll AB;

int main() {
    cin >> N >> M;
    AB = matll(M, vecll(2));
    rep(i, M) cin >> AB[i][0] >> AB[i][1];

    vecll ans = vecll(N, 0);
    repitr(ab, AB) {
        int a = ab[0] - 1, b = ab[1] - 1;
        ans[a]++, ans[b]++;
    }
    repitr(ai, ans) cout << ai << '\n';
    return 0;
}
