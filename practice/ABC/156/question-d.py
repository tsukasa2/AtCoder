def n_comb_k( n, k, MOD ):
    chld = 1
    prnt = 1
    for r in range( 1, k + 1 ):
        chld = ( chld * ( n - k + r ) ) % MOD
        prnt = ( prnt * r ) % MOD
    return chld * pow( prnt, MOD - 2, MOD ) % MOD

n, a, b = map( int, input().split() )
MOD = 10 ** 9 + 7

ans = pow( 2, n, MOD ) -1

ans = ( ans - n_comb_k( n, a, MOD ) ) % MOD
ans = ( ans - n_comb_k( n, b, MOD ) ) % MOD

print( ans )