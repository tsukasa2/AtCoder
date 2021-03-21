N = int( input() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )

ans = 0
for i in range( N ):
    if B[ i ] < A[ i ]:
        A[ i ] -= B[ i ]
        ans += B[ i ]
    else:
        if A[ i ] + A[ i + 1 ] > B[ i ]:
            A[ i + 1 ] -= B[ i ] - A[ i ]
            ans += B[ i ]
        else:
            ans += A[ i ] + A[ i + 1 ]
            A[ i ] = 0
            A[ i + 1 ] = 0

print( ans )