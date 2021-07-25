#include <bits/stdc++.h>
using namespace std;

char C;
string V = "aiueo";

int main() {
    cin >> C;
    if (V.find(C) <= 5)
        cout << "vowel" << '\n';
    else
        cout << "consonant" << '\n';
    return 0;
}
