#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B, C;

int main() {
    cin >> A >> B >> C;
    set<ll> res{A, B, C};
    cout << res.size() << '\n';

    return 0;
}
