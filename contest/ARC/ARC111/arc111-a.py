N, M = map( int, input().split() )

MOD = M ** 2

print( ( pow( 10, N, MOD ) // M ) % M )

