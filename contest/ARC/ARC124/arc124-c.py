N = int( input() )
ab = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

import math

ans = -1
def solve( i, X, Y ):
    if i == 0:
        a, b = ab[ i ]
        solve( i + 1, a, b )
    elif i == N:
        global ans
        ans = max( ans, X * ( Y // math.gcd( X, Y ) ) )
        return
    else:
        a, b = ab[ i ]
        solve( i + 1, math.gcd( X, a ), math.gcd( Y, b ) )
        solve( i + 1, math.gcd( X, b ), math.gcd( Y, a ) )

solve( 0, 1, 1 )
print( ans )