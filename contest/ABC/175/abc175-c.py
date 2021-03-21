x, k, d = map( int, input().split() )

p = x // d
q = x % d

if k < abs( p ):
    print( abs( x ) - k * d )
else:
    t = k - p
    if t % 2 == 0:
        print( q )
    else:
        print( d - q )