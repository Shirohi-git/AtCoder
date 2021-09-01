#include <bits/stdc++.h>
using namespace std;
using ll = long long;

string XY;
ll Y;

int main() {
    cin >> XY;
    Y = XY[XY.size() - 1] - '0';

    string ans;
    ans += XY[0];
    if (XY.size() == 4) ans += XY[1];
    if (0 <= Y && Y < 3) ans += '-';
    if (6 < Y && Y <= 9) ans += '+';
    cout << ans << '\n';

    return 0;
}
