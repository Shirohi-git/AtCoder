#include <bits/stdc++.h>
using namespace std;

string N;

int main() {
    cin >> N;
    string rev(N.rbegin(), N.rend());
    string ans = "No";
    if (N == rev) ans = "Yes";
    cout << ans << '\n';

    return 0;
}
