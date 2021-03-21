#include <bits/stdc++.h>
using namespace std;

int main(){
    int A, B, C, max_ABC, min_ABC;
    cin >> A >> B >> C;

    max_ABC = max( A, max( B, C ) );
    min_ABC = min( A, min( B, C ) );

    cout << ( max_ABC - min_ABC ) << endl;
}