N = int( input() )
house = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

x = []
y = []
for i, ( x_i, y_i ) in enumerate( house ):
    x.append( ( x_i, i ) )
    y.append( ( y_i, i ) )

x.sort()
y.sort()

d1 = x[ -1 ][ 0 ] - x[ 0 ][ 0 ]
d2 = y[ -1 ][ 0 ] - y[ 0 ][ 0 ]

if d1 > d2:
    max_i, max_j = x[ 0 ][ 1 ], x[ -1 ][ 1 ]
else:
    max_i, max_j = y[ 0 ][ 1 ], y[ -1 ][ 1 ]

d = [ ( x[ -1 ][ 0 ] - x[ 0 ][ 0 ], ( x[ 0 ][ 1 ], x[ -1 ][ 1 ] ) ),
    ( x[ -1 ][ 0 ] - x[ 1 ][ 0 ], ( x[ 1 ][ 1 ], x[ -1 ][ 1 ] ) ),
    ( x[ -2 ][ 0 ] - x[ 0 ][ 0 ], ( x[ 0 ][ 1 ], x[ -2 ][ 1 ] ) ),
    ( y[ -1 ][ 0 ] - y[ 0 ][ 0 ], ( y[ 0 ][ 1 ], y[ -1 ][ 1 ] ) ),
    ( y[ -1 ][ 0 ] - y[ 1 ][ 0 ], ( y[ 1 ][ 1 ], y[ -1 ][ 1 ] ) ),
    ( y[ -2 ][ 0 ] - y[ 0 ][ 0 ], ( y[ 0 ][ 1 ], y[ -2 ][ 1 ] ) ) ]

# print( d )
# print( x )
# print( y )

d.sort( reverse=True )
for ( d_i, xy_i ) in d:
    x_i, y_i = xy_i
    if set( [ max_i, max_j ] ) == set( [ x_i, y_i ] ):
        continue
    else:
        print( d_i )
        break