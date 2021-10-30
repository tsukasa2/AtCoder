N = int( input() )
XY = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

ans = 0
for i in range( N - 2 ):
    for j in range( i + 1, N - 1 ):
        for k in range( j + 1, N ):
            xi, yi = XY[ i ]
            xj, yj = XY[ j ]
            xk, yk = XY[ k ]

            ax, ay = xj - xi, yj - yi
            bx, by = xk - xi, yk - yi

            if ay * bx == ax * by:
                continue
            
            ans += 1

print( ans )