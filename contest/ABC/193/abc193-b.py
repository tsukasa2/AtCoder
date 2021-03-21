N = int( input() )
APX = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

ans = 10 ** 10
for ( a, p, x ) in APX:
    if a < x:
        ans = min( ans, p )

if ans >= 10 ** 10:
    print( -1 )
else:
    print( ans )