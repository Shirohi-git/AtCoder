#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll R, G, B;

int main() {
    cin >> R >> G >> B;
    ll num = R * 100 + G * 10 + B;

    string ans = "NO";
    if (num % 4 == 0) ans = "YES";
    cout << ans << '\n';

    return 0;
}
