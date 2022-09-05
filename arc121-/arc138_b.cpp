#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using str = string;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define all(v) (v).begin(), (v).end()

ll N;
vecll A;

int main() {
    cin >> N;
    A = vecll(N);
    rep(i, N) cin >> A[i];

    int flag = 0;
    deque<int> a(all(A));
    while (!a.empty() && ((a.front() == flag) || (a.back() == flag))) {
        if (a.back() == flag) {
            a.pop_back();
            continue;
        }
        a.pop_front();
        flag ^= 1;
    }

    str ans = "Yes";
    if (a.size() > 0) ans = "No";
    cout << ans << '\n';
    return 0;
}
