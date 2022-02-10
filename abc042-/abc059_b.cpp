#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
#define rep(i, n) for (ll i = 0; i < ll(n); i++)

string A, B;
vecll veca, vecb;

int main() {
    cin >> A >> B;
    ll la = A.size(), lb = B.size();
    ll len = max(la, lb);

    veca = vecll(len, 0), vecb = vecll(len, 0);
    rep(i, la) veca[len - la + i] = A[i] - '0';
    rep(i, lb) vecb[len - lb + i] = B[i] - '0';

    string ans = "";
    rep(i, len){
        if (veca[i] > vecb[i]) ans = "GREATER";
        if (veca[i] < vecb[i]) ans = "LESS";
        if (veca[i] != vecb[i]) break;
        if (i == len - 1) ans = "EQUAL";
    }

    cout << ans << '\n';
    return 0;
}
