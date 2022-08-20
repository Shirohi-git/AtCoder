#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using str = string;

#define repitr(id, itr) for (auto& id : (itr))
#define all(v) (v).begin(), (v).end()


str S;
str ALPs = "abcdefghijklmnopqrstuvwxyz";

template <typename T>
map<T, ll> counter(const vector<T>& vec0) {
    map<T, ll> res;
    for (auto& key : vec0) res[key]++;
    return res;
}

int main() {
    cin >> S;
    vector<char> s(all(S));
    map<char, ll> cnt = counter(s);

    str ans = "None";
    repitr(si, ALPs) if (cnt[si] == 0) {
        ans = si;
        break;
    }
    cout << ans << '\n';
    return 0;
}
