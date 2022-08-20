#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll X, A, B;

int main() {
    cin >> X >> A >> B;
    char ans = 'A';
    if (abs(X - A) > abs(X - B)) ans = 'B';
    cout << ans << '\n';
    return 0;
}
