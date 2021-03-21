#include <bits/stdc++.h>
using namespace std;

int main(){
    int i, x = 1;
    char c;
    string S;
    cin >> S;

    for( i = 0; i < S.size(); i++ ){
        c = S.at( i );
        if( c == '+' ){
            x += 1;
        }else if( c == '-' ){
            x -= 1;
        }
    }

    cout << x << endl;
}