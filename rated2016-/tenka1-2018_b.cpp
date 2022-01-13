#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;
#define rep(i, n) for (ll i = 0; i < ll(n); i++)
template <typename T>
void coutitr(const T& itr) {
    for (auto& id : itr) cout << id << ' ';
    cout << '\n';
    return;
}

ll A, B, K;

int main() {
    cin >> A >> B >> K;
    rep(i, K) {
        if (A % 2 == 1) A -= 1;
        B += A / 2, A /= 2;
        swap(A, B);
    }
    if (K % 2 == 1) swap(A, B);
    vecll ans = {A, B};
    coutitr(ans);

    return 0;
}
