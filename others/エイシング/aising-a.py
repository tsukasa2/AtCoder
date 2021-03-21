l, r, d = map( int, input().split() )

ans = 0
for k in range( l, r + 1 ):
    if k % d == 0:
        ans += 1

print( ans )