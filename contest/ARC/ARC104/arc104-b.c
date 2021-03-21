#include <stdio.h>

int main(){
    int n;
    char s[5000];
    int at[5001], gc[5001];
    int i, j;
    int ans;

    at[ 0 ] = 0;
    gc[ 0 ] = 0;
    scanf("%d %s", &n, s);

    for(i=0;i<n;i++){
        if( s[ i ] == 'A' ){
            at[ i + 1 ] = at[ i ] + 1;
            gc[ i + 1 ] = gc[ i ];
        }else if( s[ i ] == 'T' ){
            at[ i + 1 ] = at[ i ] - 1;
            gc[ i + 1 ] = gc[ i ];
        }else if( s[ i ] == 'G' ){
            at[ i + 1 ] = at[ i ];
            gc[ i + 1 ] = gc[ i ] + 1;
        }else if( s[ i ] == 'C' ){
            at[ i + 1 ] = at[ i ];
            gc[ i + 1 ] = gc[ i ] - 1;
        }
        // printf( "%d %d\n", at[ i ], gc[ i ] );        
    }

    ans = 0;
    for( i=0; i<n+1; i++ ){
        for( j=0; j<i; j++ ){
            if( at[ i ] == at[ j ] && gc[ i ] == gc[ j ] ){
                ans += 1;
            }
        }
    }
    printf( "%d\n", ans );
}