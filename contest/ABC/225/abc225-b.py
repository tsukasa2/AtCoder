N = int( input() )
ab = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]

dim = [ 0 ] * N
for a, b in ab:
    dim[ a - 1 ] += 1
    dim[ b - 1 ] += 1

if max( dim ) == N - 1:
    print( "Yes" )
else:
    print( "No" )