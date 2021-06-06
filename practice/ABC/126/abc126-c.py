import math

N, K = map( int, input().split() )

p = [ 1.0 for _ in range( N ) ]
for i in range( N ):
    p[ i ] = 0.5 ** max( 0, math.ceil( math.log2( K / ( i + 1 ) ) ) )

print( sum( p ) / N )