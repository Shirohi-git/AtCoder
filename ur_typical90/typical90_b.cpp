#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < int(n); i++)

int n;

int main() {
    cin >> n;
    if (n % 2 == 1) return 0;

    rep(i, 1 << n) {
        int a = 0, b = 0;
        vector<string> ans(n);
        rep(j, n) {
            if (i >> (n - 1 - j) & 1) {
                b++;
                ans[j] = ")";
                if (a < b) break;
            } else {
                a++;
                ans[j] = "(";
                if (a > n / 2) break;
            }
        }
        if (a == b) {
            rep(j, n) cout << ans[j];
            cout << "\n";
        }
    }
    return 0;
}
