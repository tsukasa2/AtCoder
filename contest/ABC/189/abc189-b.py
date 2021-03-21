N, X = map( int, input().split() )
sake = []
for _ in range( N ):
    V, P = map( int, input().split() )
    sake.append( ( V, P ) )

alcohol = 0
for i in range( N ):
    v, p = sake[ i ]
    alcohol += v * p
    if X * 100 < alcohol:
        print( i + 1 )
        exit()

print( -1 )