X_str, Y_str, R_str = map( str, input().split() )

def x10000( n_str ):
    if "." in n_str:
        n_int, n_float = n_str.split( "." )
        n_float = n_float.ljust( 4, "0" )
        return int( n_int + n_float )
    else:
        return int( n_str + "0000" )

X, Y, R = map( x10000, [ X_str, Y_str, R_str ] )
# print( "TEST:", X, Y, R )

import math
INF = 10 ** 6
bottom = ( Y - R ) // 10000
top = ( Y + R ) // 10000

ans = 0
for y in range( bottom, top + 1 ):
    
    z2 = ( R ** 2 - ( y * 10000 - Y ) ** 2 ) / ( 10000 ** 2 )
    if z2 < 0:
        continue

    l = -INF
    r = X // 10000
    while r - l > 1:
        m = ( l + r ) // 2
        m2 = ( m * 10000 - X ) ** 2 / ( 10000 ** 2 )
        if m2 > z2:
            l = m
        else:
            r = m
        # print( l, r )
    min_x = r

    l = X // 10000
    r = INF
    while r - l > 1:
        m = ( l + r ) // 2
        m2 = ( m * 10000 - X ) ** 2 / ( 10000 ** 2 )
        if m2 > z2:
            r = m
        else:
            l = m
        # print( l, r )
    max_x = l

    ans += max_x - min_x + 1
    # print( "TEST:", y, ans, max_x, min_x )

print( ans )