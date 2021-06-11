#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
using matll = vector<vector<ll>>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)
#define repr(i, a, b) for (ll i = ll(a); i < ll(b); i++)
#define reprs(i, a, b, s) for (ll i = ll(a); i < ll(b); i += s)
#define repdic(key, val, dic) for (const auto& [key, val] : dic)
#define sort_all(v) sort(v.begin(), v.end())
#define min_val(v) *min_element(v.begin(), v.end())
#define max_val(v) *max_element(v.begin(), v.end())
#define max_idx(v) distance(v.begin(), max_element(v.begin(), v.end()))
#define sum(v) accumulate(v.begin(), v.end(), 0LL)
#define all(v) v.begin(), v.end()
#define deg_to_rad(deg) (((deg) / 360) * 2 * M_PI)
#define rad_to_deg(rad) (((rad) / 2 / M_PI) * 360)
#define coutdeci cout << fixed << setprecision(15)

ll N;
vecll A;

int main() {
    cin >> N;
    A = vecll(N);
    rep(i, N) cin >> A[i];

    return 0;
}
