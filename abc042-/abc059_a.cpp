#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(), (v).end()

string S, T, U;

char ToUpper(char c) { return toupper(c); }

int main() {
    cin >> S >> T >> U;

    string ans = "";
    ans += S[0];
    ans += T[0];
    ans += U[0];

    transform(all(ans), ans.begin(), ToUpper);
    cout << ans << '\n';

    return 0;
}