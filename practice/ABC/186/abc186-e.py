T = int( input() )

import math

ans = []
for _ in range( T ):
    N, S, K = map( int, input().split() )

    g = math.gcd( N, K )

    if S % g != 0:
        ans.append( -1 )
        continue
    
    N //= g
    S //= g
    K //= g
    
    inv_k = pow( K, -1, N )
    ans.append( - S * inv_k % N )

for a in ans:
    print( a )