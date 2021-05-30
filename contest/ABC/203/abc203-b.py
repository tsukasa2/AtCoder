N, K = map( int, input().split() )

ans = 0

ans += ( N * ( N + 1 ) // 2 ) * 100 * K
ans += ( K * ( K + 1 ) // 2 ) * N

print( ans )