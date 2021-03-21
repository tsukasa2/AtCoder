#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;

    vector< int > A( M ), B( M );

    vector< vector< char > > R( N, vector< char >( N, '-' ) );
    for( int i = 0; i < M; i++ ){
        cin >> A.at( i ) >> B.at( i );
    }

    for( int i = 0; i < M; i++ ){
        R.at( A.at( i ) - 1 ).at( B.at( i ) - 1 ) = 'o';
        R.at( B.at( i ) - 1 ).at( A.at( i ) - 1 ) = 'x';
    }

    for( int i = 0; i < N; i++ ){
        for( int j = 0; j < N - 1; j++ ){
            cout << R.at( i ).at( j ) << " ";
        }
        cout << R.at( i ).at( N - 1 ) << endl;
    }
}