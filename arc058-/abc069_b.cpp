#include <bits/stdc++.h>
using namespace std;
using ll = long long;

string S;

int main() {
    cin >> S;
    ll cnt = S.size() - 2;
    string ans = S[0] + to_string(cnt) + S[S.size() - 1];
    cout << ans << '\n';

    return 0;
}
