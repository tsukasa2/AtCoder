N = int( input() )
X, C = [], []
for _ in range( N ):
    x, c = map( int, input().split() )
    X.append( x )
    C.append( c )

max_C = max( C )
