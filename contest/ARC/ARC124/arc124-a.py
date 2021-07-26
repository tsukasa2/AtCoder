N, K = map( int, input().split() )
ck = [ tuple( map( str, input().split() ) ) for _ in range( K ) ]
MOD = 998244353

diff = [ ( -1, "N" ) for _ in range( N ) ]
ans = 1
hand = K
for i, ( c, k ) in enumerate( ck ):
    if diff[ int( k ) - 1 ] == ( -1, "N" ):
        diff[ int( k ) - 1 ] = ( i, c )
        if c == "L":
            hand -= 1
    else:
        print( 0 )
        exit()

for i, ( k, c ) in enumerate( diff ):
    if c == "L":
        hand += 1
    elif c == "R":
        hand -= 1
    else:
        ans *= hand
        ans %= MOD

print( ans )