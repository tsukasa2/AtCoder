N, M = map( int, input().split() )
LR = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

L_max = -1
R_min = 10 ** 5 + 100
for ( L, R ) in LR:
    L_max = max( L_max, L )
    R_min = min( R_min, R )

print( max( 0, R_min - L_max + 1 ) )