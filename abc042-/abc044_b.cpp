#include <bits/stdc++.h>
using namespace std;
using ll = long long;

#define for_itr(id, itr) for (auto& id : itr)

int main() {
    string w;
    cin >> w;
    vector<ll> cnt(26, 0);

    for_itr(wi, w) cnt[wi - 'a']++;
    for_itr(ci, cnt) {
        if (ci % 2) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}
