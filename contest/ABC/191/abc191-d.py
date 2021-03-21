X, Y, R = map( int, input().split() )

R2 = R * R
ans = 0

import math

for y in range( math.ceil( Y - R ), math.floor( Y + R ) + 1 ):
    y_Y2 = ( y - Y ) * ( y - Y )

    l = math.floor( X - R - 1 )
    r = math.ceil( X )
    while r - l > 1:
        m = ( l + r ) // 2
        if ( m - X ) * ( m - X ) + y_Y2 > R2:
            l = m
        else:
            r = m
    # print( r, l )
    min_x = r

    l = math.floor( X )
    r = math.ceil( X + R + 1 )
    while r - l > 1:
        m = ( l + r ) // 2
        if ( m - X ) * ( m - X ) + y_Y2 > R2:
            r = m
        else:
            l = m
    # print( r, l )
    max_x = l

    # print( y, min_x, max_x )
    ans += max_x - min_x + 1

print( ans )