#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define sort_all(v) (sort((v).begin(), (v).end()))

ll A, B, C;

int main() {
    cin >> A >> B >> C;
    vecll abc = {A, B, C};
    sort_all(abc);

    ll ans = abc[2] - abc[1];
    abc = {abc[0] + ans, abc[2], abc[2]};

    ll diff = abc[2] - abc[0];
    ans += (diff + 1) / 2;
    if ((diff + 1) / 2 * 2 > diff) ans += 1;

    cout << ans << '\n';
    return 0;
}
