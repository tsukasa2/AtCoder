N, K = map( int, input().split() )

if K % 2 == 1:
    ans = ( N // K ) ** 3
else:
    ans = ( N // K ) ** 3 + ( ( N + K // 2 ) // K ) ** 3

print( ans )