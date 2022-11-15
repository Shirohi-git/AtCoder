#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;

ll R;

int main() {
    cin >> R;
    str ans = "ABC";
    if (R >= 1200) ans = "ARC";
    if (R >= 2800) ans = "AGC";
    cout << ans << '\n';
    return 0;
}
