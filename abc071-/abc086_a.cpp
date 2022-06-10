#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B;

int main() {
    cin >> A >> B;
    string ans = "Even";
    if (A % 2 == 1 && B % 2 == 1) ans = "Odd";
    cout << ans << '\n';
    return 0;
}
