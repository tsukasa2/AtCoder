#include <bits/stdc++.h>
using namespace std;

int main(){
    long long H, W, N, M;
    cin >> H >> W >> N >> M;

    vector< long long > A( N ), B( N ); 
    vector< long long > C( M ), D( M );

    for( long long i = 0; i < N; i++ ){
        cin >> A.at( i ) >> B.at( i );
    }

    for( long long i = 0; i < M; i++ ){
        cin >> C.at( i ) >> D.at( i );
    }

    vector< vector< long long > > field( H, vector< long long >( W, 0 ) );
    for( long long i = 0; i < N; i++ ){
        field.at( A.at( i ) - 1 ).at( B.at( i ) - 1 ) = 2;
    }
    for( long long i = 0; i < M; i++ ){
        field.at( C.at( i ) - 1 ).at( D.at( i ) - 1 ) = -1;
    }

    long long ans = N;
    long long i, j;
    vector< vector< bool > > arrived_h( H, vector< bool >( W, false ) );
    for( long long k = 0; k < N; k++ ){
        i = A.at( k ) - 1, j = B.at( k ) - 1;
        if( arrived_h.at( i ).at( j ) ){
            continue;
        }
        //W
        i = A.at( k ) - 1, j = B.at( k ) - 1;
        for( long long d = 1; d < H + 1; d++ ){
            if( i - d < 0 ){
                break;
            }else if( field.at( i - d ).at( j ) == -1 ){
                break;
            }else if( field.at( i - d ).at( j ) == 0 ){
                field.at( i - d ).at( j ) = 1;
                ans++;
            }
            arrived_h.at( i - d ).at( j ) = true;
        }
        //S
        i = A.at( k ) - 1, j = B.at( k ) - 1;
        for( long long d = 1; d < H + 1; d++ ){
            if( i + d >= H ){
                break;
            }else if( field.at( i + d ).at( j ) == -1 ){
                break;
            }else if( field.at( i + d ).at( j ) == 0 ){
                field.at( i + d ).at( j ) = 1;
                ans++;
            }
            arrived_h.at( i + d ).at( j ) = true;
        }
    }

    vector< vector< bool > > arrived_v( H, vector< bool >( W, false ) );
    for( long long k = 0; k < N; k++ ){
        i = A.at( k ) - 1, j = B.at( k ) - 1;
        if( arrived_v.at( i ).at( j ) ){
            continue;
        }
        //A
        i = A.at( k ) - 1, j = B.at( k ) - 1;
        for( long long d = 1; d < W + 1; d++ ){
            if( j - d < 0 ){
                break;
            }else if( field.at( i ).at( j - d ) == -1 ){
                break;
            }else if( field.at( i ).at( j - d ) == 0 ){
                field.at( i ).at( j - d ) = 1;
                ans++;
            }
            arrived_v.at( i ).at( j - d ) = true;
        }
        //D
        i = A.at( k ) - 1, j = B.at( k ) - 1;
        for( long long d = 1; d < W + 1; d++ ){
            if( j + d >= W ){
                break;
            }else if( field.at( i ).at( j + d ) == -1 ){
                break;
            }else if( field.at( i ).at( j + d ) == 0 ){
                field.at( i ).at( j + d ) = 1;
                ans++;
            }
            arrived_v.at( i ).at( j + d ) = true;
        }
    }

    // for( int i = 0; i < H; i++ ){
    //     for( int j = 0; j < W; j++ ){
    //         cout << field.at( i ).at( j ) << "\t";
    //     }
    //     cout << endl;
    // }

    cout << ans << endl;
}