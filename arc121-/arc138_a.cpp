#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

#define rep(i, n) for (ll i = 0; i < ll(n); i++)
#define reprms(i, a, b, s) for (ll i = ll(a); i > ll(b); i += (s))
#define unique_sort(v)              \
    (sort((v).begin(), (v).end())); \
    ((v).erase(unique((v).begin(), (v).end()), (v).end()))

ll N, K;
vecll A;

template <typename T>
class Compression {
   public:
    ll len = 0;
    map<T, ll> dic;
    vector<T> vec = {};

    Compression(const vector<T>& itr) {
        vec.resize(itr.size());
        copy(itr.begin(), itr.end(), vec.begin());
        unique_sort(vec);
        len = vec.size();
        rep(i, len) dic[vec[i]] = i;
    }

    ll zip(T key) { return dic[key]; }

    T unzip(ll idx) { return vec[idx]; }
};

int main() {
    cin >> N >> K;
    A = vecll(N);
    rep(i, N) cin >> A[i];

    Compression cmp(A);
    vecll idx_min(cmp.len + 1, 3 * N);
    reprms(i, N - 1, K - 1, -1) {
        ll ci = cmp.zip(A[i]);
        idx_min[ci] = i - K;
    }
    reprms(i, cmp.len - 2, -1, -1) {
        idx_min[i] = min(idx_min[i + 1], idx_min[i]);
    }

    ll ans = 3 * N;
    rep(i, K) {
        ll res = K - i;
        res += idx_min[cmp.zip(A[i]) + 1];
        ans = min(ans, res);
    }
    if (ans == 3 * N) ans = -1;
    cout << ans << '\n';

    return 0;
}
