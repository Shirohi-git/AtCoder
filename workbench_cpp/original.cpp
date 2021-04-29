#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < int(n); i++)
#define repi(i, a, b) for (int i = int(a); i < int(b); ++i)

ll n;
vector<ll> a(pow(10, 6));

int main() {
    cin >> n;
    rep(i, n) { cin >> a[i]; }
    return 0;
}
