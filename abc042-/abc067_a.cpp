#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B;

int main() {
    cin >> A >> B;
    string ans = "Impossible";
    if (A % 3 == 0 || B % 3 == 0) ans = "Possible";
    if ((A + B) % 3 == 0) ans = "Possible";

    cout << ans << '\n';

    return 0;
}
