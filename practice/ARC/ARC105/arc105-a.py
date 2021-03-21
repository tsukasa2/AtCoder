a, b, c, d = map( int, input().split() )

if a + b == c + d:
    print( "Yes" )
elif a + c == b + d:
    print( "Yes" )
elif a + d == b + c:
    print( "Yes" )
elif a == b + c + d:
    print( "Yes" )
elif b == c + d + a:
    print( "Yes" )
elif c == d + a + b:
    print( "Yes" )
elif d == a + b + c:
    print( "Yes" )
else:
    print( "No" )