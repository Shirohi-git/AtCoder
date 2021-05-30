#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < int(n); i++)

long long n, l, k;
vector<long long> a(pow(10, 6));

bool isOK(int res) {
    int cnt = 0, bfo = 0;
    rep(i, n) {
        if (a[i] - bfo >= res && l - a[i] >= res) {
            cnt++;
            bfo = a[i];
        }
    }
    if (cnt >= k)
        return true;
    else
        return false;
}

int binary_search() {
    int left = -1, right = l + 1;
    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        if (isOK(mid) == false)
            right = mid;
        else
            left = mid;
    }
    return left;
}

int main() {
    int ans;
    cin >> n >> l >> k;
    rep(i, n) { cin >> a[i]; }
    ans = binary_search();
    cout << ans << endl;
    return 0;
}

