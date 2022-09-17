#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;

ll A, B;

int main() {
    cin >> A >> B;
    str ans = "Yes";
    if (A * B % 2 == 0) ans = "No";
    cout << ans << '\n';
    return 0;
}
