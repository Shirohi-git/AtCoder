#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
#define is_exist(v, itm) (*find((v).begin(), (v).end(), itm) == itm)

ll N;

int main() {
    cin >> N;

    vecll a = {3, 5, 7};
    string ans = "NO";
    if (is_exist(a, N)) ans = "YES";

    cout << ans << '\n';
    return 0;
}
