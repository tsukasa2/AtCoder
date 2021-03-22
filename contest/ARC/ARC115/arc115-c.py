N = int( input() )

A = [ 1 for _ in range( N ) ]

for i in range( 1, N + 1 ):
    j = i
    a = A[ j - 1 ]
    j += i
    while j - 1 < N:
        if a == A[ j - 1 ]:
            A[ j - 1 ] += 1
        j += i

print( " ".join( map( str, A ) ) )