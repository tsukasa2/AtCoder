T = int( input() )

def extGCD( a, b ):
    # ax + by = gcd( a, b ) を解く
    if b == 0:
        return 1, 0, a
    else:
        y, x, d = extGCD( b, a % b )
        return x, y - x * a // b, d

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
    
    x, _, _ = extGCD( K, N )
    ans.append( - x * S % N )

for a in ans:
    print( a )