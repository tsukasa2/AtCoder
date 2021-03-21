x, y = map( int, input().split() )

if y < 2 * x or 4 * x < y or y % 2 == 1:
    print( "No" )
else:
    print( "Yes" )