import math

A, B, W = map( int, input().split() )
W *= 1000

Q = W // A
if B * Q < W:
    print( "UNSATISFIABLE" )
    exit()

most = math.floor( W / A )
least = math.ceil( W / B )
print( least, most )