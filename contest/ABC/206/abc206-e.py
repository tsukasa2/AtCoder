L, R = map( int, input().split() )

import math

ans = 0
for k in range( max( 2, math.ceil( L // 2 ) ), R // 2 + 1 ):
    l = k * math.ceil( max( 2, L / k ) )
    r = ( R // k ) * k

    for i in range( l, r + 1, k ):
        ans_k = ( r - i ) // k
        ans_k -= R // i - ( L - 1 ) // i
        if i >= L:
            ans_k += 1
    
        print( k, i, ans_k )
        ans += ans_k

print( ans * 2 )