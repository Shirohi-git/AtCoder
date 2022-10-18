#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecc = vector<char>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)

template <typename T>
void coutitr(const T& itr) {
    for (auto& id : itr) cout << id;
    cout << '\n';
    return;
}

vecc A;

int main() {
    A = vecc(3);
    rep(i, 3) cin >> A[i];

    rep(i, 3) {
        if (A[i] == '1')
            A[i] = '9';
        else if (A[i] == '9')
            A[i] = '1';
    }
    coutitr(A);
    return 0;
}
