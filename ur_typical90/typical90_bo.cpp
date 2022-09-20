#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define repitr(id, itr) for (auto& id : itr)

string NUM8;
ll K;

string base_8to10to8(string num8) {
    ll num10 = 0;
    repitr(num, num8) num10 = num10 * 8 + ll(num - '0');

    if (num10 == 0) return "0";
    string res = "";
    while (num10) {
        char add = char(num10 % 9 + '0');
        if (add == '8') add = '5';
        res = add + res, num10 /= 9;
    }
    return res;
}

int main() {
    cin >> NUM8 >> K;

    string num8 = NUM8;
    rep(_, K) num8 = base_8to10to8(num8);
    cout << num8 << endl;
    return 0;
}
