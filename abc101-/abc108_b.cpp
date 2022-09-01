#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

template <typename T>
void coutitr(const T& itr) {
    for (auto& id : itr) cout << id << ' ';
    cout << '\n';
    return;
}

ll X1, Y1, X2, Y2;

int main() {
    cin >> X1 >> Y1 >> X2 >> Y2;

    ll x21 = X2 - X1, y21 = Y2 - Y1;
    vecll ans = {X2 - y21, Y2 + x21, X1 - y21, Y1 + x21};
    coutitr(ans);
    return 0;
}
