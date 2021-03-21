def modinv( n, MOD ):
    if n == 0:
        return 1
    if ( MOD + 1 ) % n == 0:
        return ( MOD + 1 ) // n
    inv_n = ( -modinv( MOD % n, MOD ) * ( MOD // n ) ) % MOD
    return inv_n

T = int( input() )
ans = []

for _ in range( T ):
    N, S, K = map( int, input().split() )

    if K % N == 0:
        ans.append( -1 )
        continue
    
    if N % K == 0 and ( N - S ) % K != 0:
        ans.append( -1 )
        continue
    
    ans.append( modinv( K, N ) )

for a in ans:
    print( a )