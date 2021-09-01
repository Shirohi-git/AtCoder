#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define all(v) v.begin(), v.end()

ll N;
int main() {
    cin >> N;
    string ans;

    while (N > 0) {
        if (N % 2 == 0) ans += 'B', N /= 2;
        if (N % 2 == 1) ans += 'A', N--;
    }
    reverse(all(ans));
    cout << ans << '\n';
    return 0;
}
