#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll A, B;

int main() {
    cin >> A >> B;
    if (A + B < 10)
        cout << A + B << '\n';
    else
        cout << "error" << '\n';

    return 0;
}
