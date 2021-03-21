N = int( input() )
S = str( input() )
X = str( input() )

DP = [ [ "Aoki" for _ in range( N + 1 ) ] for _ in range( 7 ) ]

if X[ -1 ] == "T":
    for i in range( 7 ):
        if i % 7 == 0 or ( i + int( S[ -1 ] ) ) % 7 == 0:
            DP[ i ][ 1 ] = "Takahashi"
else:
    for i in range( 7 ):
        if i % 7 == 0 and ( i + int( S[ -1 ] ) ) % 7 == 0:
            DP[ i ][ 1 ] = "Takahashi"

for i in range( 1, N + 1 ):
    x = X[ i - 1 ]
    if x == "T":
        for j in range( 7 ):
            if j % 7 == 0 or ( j + int( S[ N - i ] ) ) % 7 == 0:
                DP[ j ][ i ] = "Takahashi"
    else:
        for j in range( 7 ):
            if j % 7 == 0 and ( j + int( S[ N - i ] ) ) % 7 == 0:
                DP[ j ][ i ] = "Takahashi"

print( DP[ 0 ][ N ] )