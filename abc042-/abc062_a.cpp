#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define all(v) (v).begin(), (v).end()
#define in_vec(v, x) (*find((v).begin(), (v).end(), (x)) == (x))

ll X, Y;

int main() {
    cin >> X >> Y;
    vecll a = {1, 3, 5, 7, 8, 10, 12};
    vecll b = {4, 6, 9, 11};

    string ans = "No";
    if (in_vec(a, X) & in_vec(a, Y)) ans = "Yes";
    if (in_vec(b, X) & in_vec(b, Y)) ans = "Yes";
    cout << ans << '\n';

    return 0;
}
