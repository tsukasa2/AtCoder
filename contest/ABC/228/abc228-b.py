N, X = map( int, input().split() )
A = list( map( int, input().split() ) )

visited = [ 0 ] * N
x = X
while visited[ x - 1 ] == 0:
    visited[ x - 1 ] = 1
    x = A[ x - 1 ]

print( sum( visited ) )