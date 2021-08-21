N, M = map( int, input().split() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

AB.sort()
drinks = 0
ans = 0
for ( a, b ) in AB:
    if drinks + b < M:
        drinks += b
        ans += a * b
    else:
        ans += a * ( M - drinks )
        break

print( ans )