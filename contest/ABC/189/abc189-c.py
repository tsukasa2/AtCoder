N = int( input() )
A = list( map( int, input().split() ) )

ans = -1
for l in range( N ):
    x = A[ l ]
    for r in range( l, N ):
        x = min( A[ r ], x )
        ans = max( ans, x * ( r + 1 - l ) )

print( ans )