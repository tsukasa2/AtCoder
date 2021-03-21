#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, i, sum_A, avr_A;
    cin >> N;

    vector<int> A( N, 0 );
    sum_A = 0;
    for( i = 0; i < N; i++ ){
        cin >> A.at( i );
        sum_A += A.at( i );
    }

    avr_A = sum_A / N;

    for( i = 0; i < N; i++ ){
        if( A.at( i ) > avr_A ){
            cout << ( A.at( i ) - avr_A ) << endl;
        }else{
            cout << ( avr_A - A.at( i ) ) << endl;
        }
    }
}