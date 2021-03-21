N = int( input() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

ans = 10 ** 7
for i in range( N ):
    for j in range( N ):
        a = AB[ i ][ 0 ]
        b = AB[ j ][ 1 ]
        if i == j:
            ans = min( ans, a + b )
        else:
            ans = min( ans, max( a, b ) )

print( ans )