H, W = map( int, input().split() )
S = [ str( input() ) + "#" for _ in range( H ) ]
S.append( "#" * ( W + 1 ) )

blocks_h = [ [] for _ in range( H + 1 ) ]
blocks_v = [ [] for _ in range( W + 1 ) ]
for i in range( H + 1 ):
    for j in range( W + 1 ):
        if S[ i ][ j ] == "#":
            blocks_h[ i ].append( j )
            blocks_v[ j ].append( i )

lamps = [ [ 0 for _ in range( W ) ] for _ in range( H ) ]
for i in range( H ):
    k = 0
    l = -1
    r = blocks_h[ i ][ k ]
    for j in range( W ):
        if j == r:
            k += 1
            l = r
            r = blocks_h[ i ][ k ]
        else:
            lamps[ i ][ j ] += r - l - 1

for j in range( W ):
    k = 0
    l = -1
    r = blocks_v[ j ][ k ]
    for i in range( H ):
        if i == r:
            k += 1
            l = r
            r = blocks_v[ j ][ k ]
        else:
            lamps[ i ][ j ] += r - l - 2

print( max( [ max( lamps[ i ] ) for i in range( H ) ] ) )