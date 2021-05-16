#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using matdb = vector<vector<double>>;

#define all(v) v.begin(), v.end()
#define min_itr(v) *min_element(v.begin(), v.end())
#define sort_all(v) sort(v.begin(), v.end())
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define rad_to_deg(rad) (((rad) / 2 / M_PI) * 360)
#define cout_deci cout << fixed << setprecision(10)

int main() {
    ll n;
    cin >> n;
    matdb xy(n, vector<double>(2, 0));
    rep(i, n) cin >> xy[i][0] >> xy[i][1];
    const vector<double> INI(n - 1, 0);
    double ans = 180.0;

    rep(i, n) {
        vector<double> deg = INI;
        ll idx = 0;
        rep(j, n) {
            if (i == j) continue;
            double p = xy[j][0] - xy[i][0], q = xy[j][1] - xy[i][1];
            double tmp = rad_to_deg(atan2(q, p));
            if (tmp < 0.0) tmp += 360;
            deg[idx] = tmp, idx++;
        }
        sort_all(deg), deg.push_back(deg[0] + 360.0);
        deg.insert(deg.begin(), deg[n - 2] - 360.0);
        rep(j, n - 1) {
            double tmp = deg[j + 1] + 180.0;
            if (tmp >= 360.0) tmp -= 360.0;
            auto pos = upper_bound(all(deg), tmp);
            vector<double> res = {ans, tmp - *(pos - 1), *pos - tmp};
            ans = min_itr(res);
        }
    }
    cout_deci << 180.0 - ans << endl;
    return 0;
}
