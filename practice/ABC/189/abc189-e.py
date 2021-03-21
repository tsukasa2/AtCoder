N = int( input() )
XY = [ list( map( int, input().split() ) ) for _ in range( N ) ]
M = int( input() )
OP = [ list( map( int, input().split() ) ) for _ in range( M ) ]
Q = int( input() )
AB = [ list( map( int, input().split() ) ) for _ in range( Q ) ]

def mul( S, T ): # 3*3行列同士の積
    ret = [ 0 for _ in range( 9 ) ]
    for i in range( 3 ):
        for j in range( 3 ):
            for k in range( 3 ):
                ret[ i * 3 + j ] += S[ i * 3 + k ] * T[ k * 3 + j ]
    return ret

move = [
    [ 0, 1, 0, -1, 0, 0, 0, 0, 1 ],
    [ 0, -1, 0, 1, 0, 0, 0, 0, 1 ],
    [ -1, 0, 0, 0, 1, 0, 0, 0, 1 ], # index = 2 に 2 * p が入る
    [ 1, 0, 0, 0, -1, 0, 0, 0, 1 ]  # index = 5 に 2 * p が入る
]

T = [ [ 1, 0, 0, 0, 1, 0, 0, 0, 1 ] ]
for op in OP:
    i = op[ 0 ]
    if i == 1 or i == 2:
        S = move[ i - 1 ]
    elif i == 3:
        p = op[ 1 ]
        S = move[ i - 1 ]
        S[ 2 ] = 2 * p
    else:
        p = op[ 1 ]
        S = move[ i - 1 ]
        S[ 5 ] = 2 * p
    T.append( mul( S, T[ -1 ] ) )

for ( a, b ) in AB:
    xy = XY[ b - 1 ]
    xy.append( 1 )
    T_i = T[ a ]
    moved_xy = [ 0, 0, 0 ]
    for i in range( 3 ):
        for j in range( 3 ):
            moved_xy[ i ] += T_i[ i * 3 + j ] * xy[ j ]
    print( moved_xy[ 0 ], moved_xy[ 1 ] )