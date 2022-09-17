#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;
using vecs = vector<string>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : (itr))

ll N;
vecs W;

int main() {
    cin >> N;
    W = vecs(N);
    rep(i, N) cin >> W[i];

    str ans = "Yes";
    set<str> s;
    char last = W[0][0];
    repitr(wi, W) {
        if (s.find(wi) != s.end() || last != wi[0]) {
            ans = "No";
            break;
        }
        s.insert(wi);
        last = wi[wi.size() - 1];
    }
    cout << ans << '\n';
    return 0;
}
