#include <bits/stdc++.h>
using namespace std;
using str = string;
using ll = long long;
using vecc = vector<char>;

#define reprs(i, a, b, s) for (ll i = ll(a); i < ll(b); i += (s))

template <typename T>
void coutitr(const T& itr) {
    for (auto& id : itr) cout << id;
    cout << '\n';
    return;
}

str S;

int main() {
    cin >> S;
    vecc ans(0);
    reprs(i, 0, S.size(), 2) ans.push_back(S[i]);
    coutitr(ans);
    return 0;
}
