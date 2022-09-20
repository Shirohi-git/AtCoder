#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B;
const ll pow18 = 1e18;

int main() {
    cin >> A >> B;
    ll ans = B / gcd(A, B);
    if (ans > pow18 / A)
        cout << "Large" << endl;
    else
        cout << ans * A << endl;
    return 0;
}