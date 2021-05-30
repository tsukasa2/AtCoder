N, M = map( int, input().split() )
BLACK = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

BLACK.sort()

from collections import defaultdict
is_reached = defaultdict( lambda: False )
ans = 0

is_reached[ ( 0, N ) ] = True
for ( x, y ) in BLACK:
    if is_reached[ ( x - 1, y ) ] == True:
        ans -= 1
    
    if is_reached[ ( x - 1, y - 1 ) ] == True:
        if is_reached[ ( x - 1, y ) ] == False:
            ans += 1

        is_reached[ ( x, y ) ] = True
    
    if is_reached[ ( x - 1, y + 1 ) ] == True:
        if is_reached[ ( x - 1, y ) ] == False:
            ans += 1

        is_reached[ ( x, y ) ] = True
    
    print( ans )

print( is_reached )
print( max( ans, 0 ) )