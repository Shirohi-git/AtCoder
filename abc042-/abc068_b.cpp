#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define repitr(id, itr) for (auto& id : itr)

ll N;
vecll POW2 = {1, 2, 4, 8, 16, 32, 64};

int main() {
    cin >> N;
    ll ans = 0;
    repitr(num, POW2) if (num <= N) ans = num;
    cout << ans << '\n';

    return 0;
}
