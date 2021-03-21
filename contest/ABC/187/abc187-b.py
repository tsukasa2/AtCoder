N = int( input() )
x, y = [], []
for _ in range( N ):
    a, b = map( int, input().split() )
    x.append( a )
    y.append( b )

ans = 0
for i in range( N ):
    for j in range( i + 1, N ):
        s, t = x[ i ], y[ i ]
        u, v = x[ j ], y[ j ]

        m = ( t - v ) / ( s - u )
        if m >= -1 and m <= 1:
            ans += 1

print( ans )