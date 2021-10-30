H, W, N = map( int, input().split() )
r, c, a = [], [], []
for _ in range( N ):
    r_i, c_i, a_i = map( int, input().split() )
    r.append( r_i - 1 )
    c.append( c_i - 1 )
    a.append( a_i )

rci = {}
for i in range( N ):
    try:
        rci[ a[ i ] ].append( ( r[ i ], c[ i ], i ) )
    except KeyError:
        rci[ a[ i ] ] = [ ( r[ i ], c[ i ], i ) ]

DP = [ 0 ] * N
rmax = [ -1 ] * H
cmax = [ -1 ] * W
for x in sorted(
    list( rci.keys() ), reverse = True
):
    for r_i, c_i, i in rci[ x ]:
        DP[ i ] = max( [ DP[ i ], rmax[ r_i ], cmax[ c_i ] ] )
    
    for r_i, c_i, i in rci[ x ]:
        rmax[ r_i ] = max( rmax[ r_i ], DP[ i ] + 1 )
        cmax[ c_i ] = max( cmax[ c_i ], DP[ i ] + 1 )

print( *DP, sep = "\n" )