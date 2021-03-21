N = int( input() )
koma = []
for _ in range( N ):
    X, Y = map( int, input().split() )
    koma.append( ( X, Y ) )

M = int( input() )
op = []
for _ in range( M ):
    op_i = list( map( int, input().split() ) )
    op.append( op_i )

Q = int( input() )
AB = []
for _ in range( Q ):
    A, B = map( int, input().split() )
    AB.append( ( A, B ) )

