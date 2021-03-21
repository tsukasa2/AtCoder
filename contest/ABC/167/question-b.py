a, b, c, k = map( int, input().split() )

if k <= a:
    print( k )
elif k <= a + b:
    print( a )
else:
    d = k - ( a + b )
    print( a - d )