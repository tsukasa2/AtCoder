#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;

    vector< int > A( N );
    for( int i = 0; i < N; i++ ){
        cin >> A.at( i );
    }

    map< int, int > dict;
    for( int i = 0; i < N; i++ ){
        if( dict.count( A.at( i ) ) ){
            int tmp = dict.at( A.at( i ) );
            dict.erase( A.at( i ) );
            dict[ A.at( i ) ] = tmp + 1;
        }else{
            dict[ A.at( i ) ] = 1;
        }
    }

    int index = 0, most = 0;
    for( int i = 0; i < N; i++ ){
        int c = dict.at( A.at( i ) );
        if( c > most ){
            most = c;
            index = A.at( i );
        }
    }

    cout << index << " " << most << endl;
}