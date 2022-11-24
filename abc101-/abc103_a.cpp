#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B, C;

int main() {
    cin >> A >> B >> C;
    ll ans = A + B + C;
    ans = min(ans, abs(B - A) + abs(C - B));
    ans = min(ans, abs(C - A) + abs(B - C));
    ans = min(ans, abs(A - B) + abs(C - A));
    ans = min(ans, abs(C - B) + abs(A - C));
    ans = min(ans, abs(A - C) + abs(B - A));
    ans = min(ans, abs(B - C) + abs(A - B));
    cout << ans << '\n';
    return 0;
}
