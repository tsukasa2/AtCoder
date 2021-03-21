a, b, x, y = map( int, input().split() )

if 2 * x > y:
    if a > b:
        print( x + ( a - b - 1 ) * y )
    else:
        print( x + ( b - a ) * y )
else:
    if a > b:
        print( ( 2 * ( a - b ) - 1 ) * x )
    else:
        print( ( 2 * ( b - a ) + 1 ) * x )