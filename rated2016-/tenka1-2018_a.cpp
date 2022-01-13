#include <bits/stdc++.h>
using namespace std;
#define all(v) v.begin(), v.end()

string S;

int main() {
    cin >> S;
    if (S.length() == 3) reverse(all(S));
    cout << S << '\n';

    return 0;
}
