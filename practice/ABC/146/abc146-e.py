N, K = map( int, input().split() )
A = list( map( int, input().split() ) )

for i in range( N ):
    A[ i ] = A[ i ] % K

cum_sum = [ 0 ]
for i in range( N ):
    cum_sum.append( ( cum_sum[ -1 ] + A[ i ] ) % K )

print( cum_sum )