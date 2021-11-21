MOD = 998244353
N, K, M = map( int, input().split() )

# ans = 1
# for _ in range( K ** N ):
#     ans *= M
#     ans %= MOD

# print( ans )

if M % MOD == 0:
    print( 0 )
else:
    r = pow( K, N, MOD - 1 )
    ans = pow( M, r, MOD )
    print( ans )