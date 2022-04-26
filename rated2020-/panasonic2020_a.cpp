#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vecll = vector<ll>;

ll K;
vecll A;

int main() {
    cin >> K;
    A = {1, 1, 1, 2, 1, 2, 1, 5,  2, 2, 1, 5, 1, 2, 1, 14,
         1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51};
    cout << A[K - 1] << '\n';

    return 0;
}
