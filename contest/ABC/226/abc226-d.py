import math

N = int( input() )
xy = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

m = set()
for i in range( N ):
    for j in range( N ):
        if i == j:
            continue
        
        x_i, y_i = xy[ i ]
        x_j, y_j = xy[ j ]
        dx, dy = x_j - x_i, y_j - y_i

        g = math.gcd( dx, dy )
        dx //= g
        dy //= g

        m.add( ( dx, dy ) )
        # print( dx, dy )

print( len( m ) )