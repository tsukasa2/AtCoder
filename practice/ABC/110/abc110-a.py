A, B, C = map( int, input().split() )

A, B, C = sorted( [ A, B, C ] )
print( A + B + 10 * C )