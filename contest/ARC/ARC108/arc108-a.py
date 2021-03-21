import math

S, P = map( int, input().split() )

for N in range( 1, int( math.sqrt( P ) + 1 ) ):
    if P % N == 0:
        M = P // N
        if N + M == S:
            print( "Yes" )
            break
else:
    print( "No" )