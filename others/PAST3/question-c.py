a, r, n = map( int, input().split() )
LIMIT = 10 ** 9

import math

if r == 1:
    if a > LIMIT:
        print( "large" )
    else:
        print( a )
else:
    m = math.log( LIMIT / a, r )
    if m < n - 1:
        print( "large" )
    else:
        print( a * ( r ** ( n - 1 ) ) )