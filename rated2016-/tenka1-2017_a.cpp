#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define repitr(id, itr) for (auto& id : itr)

string N;

int main() {
    cin >> N;

    ll ans = 0;
    repitr(ni, N) if (ni == '1') ans += 1;
    cout << ans << '\n';

    return 0;
}
