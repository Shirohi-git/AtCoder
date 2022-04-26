#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll N, K;
string S;

int main() {
    cin >> N >> S >> K;

    char sk = S[K - 1];
    string ans = "";
    repitr(si, S) {
        if (si == sk)
            ans += si;
        else
            ans += '*';
    }
    cout << ans << '\n';

    return 0;
}
