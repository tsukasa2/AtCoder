N, K, A = map( int, input().split() )

print( ( A - 1 + K - 1 ) % N + 1 )