N = int( input() )

ans = 0

ans += max( 0, N - 999 )
ans += max( 0, N - 999999 )
ans += max( 0, N - 999999999 )
ans += max( 0, N - 999999999999 )
ans += max( 0, N - 999999999999999 )

print( ans )