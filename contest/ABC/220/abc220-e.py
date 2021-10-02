N, D = map( int, input().split() )
MOD = 998244353

ans = 0
for x in range( ( D + 1 ) // 2 ):
    y = D - x
    z = N - max( x, y )


    d_ans = pow( 2, max( 0, x - 1 ), MOD ) * pow( 2, max( 0, y - 1 ), MOD ) % MOD
    d_ans = pow( 2, max( 0, x - 1 ) + max( 0, y - 1 ), MOD )
    d_ans = d_ans * 2 * ( pow( 2, max( 0, z ), MOD ) - 1 ) % MOD
    ans = ( ans + d_ans ) % MOD

ans = ans * 2 % MOD

if D % 2 == 0:
    x = D // 2
    y = D - x
    z = N - max( x, y )


    d_ans = pow( 2, max( 0, x - 1 ), MOD ) * pow( 2, max( 0, y - 1 ), MOD ) % MOD
    d_ans = pow( 2, max( 0, x - 1 ) + max( 0, y - 1 ), MOD )
    d_ans = d_ans * 2 * ( pow( 2, max( 0, z ), MOD ) - 1 ) % MOD
    ans = ( ans + d_ans ) % MOD

print( ans )