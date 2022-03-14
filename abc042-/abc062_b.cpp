#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecs = vector<string>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

ll H, W;
vecs A;

int main() {
    cin >> H >> W;
    A = vecs(H);
    rep(i, H) cin >> A[i];

    string frame = "##";
    rep(i, W) frame += "#";

    cout << frame << '\n';
    repitr(ai, A) cout << '#' << ai << '#' << '\n';
    cout << frame << '\n';

    return 0;
}
