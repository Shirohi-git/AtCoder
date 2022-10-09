#include <bits/stdc++.h>
using namespace std;
using str = string;

char N, M;

int main() {
    cin >> N >> M;
    str ans = "No";
    if (N == '9' || M == '9') ans = "Yes";
    cout << ans << '\n';
    return 0;
}
