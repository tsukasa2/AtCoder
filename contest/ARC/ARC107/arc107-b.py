N, K = map( int, input().split() )

ans = 0
for ab in range( max( 2, 2 + K ), min( 2 * N, 2 * N + K ) + 1 ):
    cd = ab - K
    if ab <= N + 1:
        if cd <= N + 1:
            ans += ( ab - 1 ) * ( cd - 1 )
        else:
            ans += ( ab - 1 ) * ( 2 * N + 1 - cd )
    else:
        if cd <= N + 1:
            ans += ( 2 * N + 1 - ab ) * ( cd - 1 )
        else:
            ans += ( 2 * N + 1 - ab ) * ( 2 * N + 1 - cd )

print( ans )
