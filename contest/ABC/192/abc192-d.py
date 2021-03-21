X = str( input() )
M = int( input() )

d = int( sorted( X )[ -1 ] )

def f( n ):
    res = 0
    for i, c in enumerate( reversed( X ) ):
        res += int( c ) * pow( n, i )
    return res

r = M + 1
l = d + 1
if f( l ) > M:
    print( 0 )
elif len( X ) == 1:
    print( 1 )
else:
    while r - l > 1:
        m = ( l + r ) // 2
        if f( m ) > M:
            r = m
        else:
            l = m

    print( l - d )
