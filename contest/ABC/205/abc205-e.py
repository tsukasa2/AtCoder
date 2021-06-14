N, M, K = map( int, input().split() )
MOD = 10 ** 9 + 7

dp = [ [ 0 ] * ( M + 1 ) for _ in range( N + 1 ) ]
for i in range( N + 1 ):
    for j in range( M + 1 ):
        if i > j + K:
            dp[ i ][ j ] = 0
        else:
            if i == 0 or j == 0:
                dp[ i ][ j ] = 1
            else:
                dp[ i ][ j ] = ( dp[ i - 1 ][ j ] + dp[ i ][ j - 1 ] ) % MOD

print( dp[ -1 ][ -1 ] )