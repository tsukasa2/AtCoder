a, b, c = map( int, input().split() )
k = int( input() )

def solve( a, b, c, k ):
    if a < b and b < c:
        print( "Yes" )
        exit()
    elif k == 0:
        return
    else:
        solve( 2 * a, b, c, k - 1 )
        solve( a, 2 * b, c, k - 1 )
        solve( a, b, 2 * c, k - 1 )

solve( a, b, c, k )
print( "No" )