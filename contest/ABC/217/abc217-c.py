N = int( input() )
p = list( map( int, input().split() ) )

q = [ 0 ] * N
for i, x in enumerate( p ):
    q[ x - 1 ] = i + 1

print( *q, sep = " " )