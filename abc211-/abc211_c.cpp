#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define repitr(id, itr) for (auto& id : itr)

string S, C = "_chokudai";
const ll MOD1 = 1e9 + 7;

int main() {
    cin >> S;

    vecll cnt(9, 0);
    cnt[0] = 1;
    repitr(si, S) {
        ll idx = C.find(si);
        if (idx < 9) cnt[idx] = (cnt[idx] + cnt[idx - 1]) % MOD1;
    }
    cout << cnt[8] << endl;

    return 0;
}
