N, P = map( int, input().split() )
a = list( map( int, input().split() ) )

ans = 0
for a_i in a:
    if a_i < P:
        ans += 1

print( ans )