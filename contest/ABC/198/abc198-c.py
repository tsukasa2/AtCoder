import math

R, X, Y = map( int, input().split() )

if math.sqrt( X * X + Y * Y ) < R:
    print( 2 )
else:
    print( math.ceil( math.sqrt( X * X + Y * Y ) / R ) )