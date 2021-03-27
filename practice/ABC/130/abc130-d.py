N, K = map( int, input().split() )
a = list( map( int, input().split() ) )

# s = a[ l ] + a[ l + 1 ] + ... + a[ r - 1 ]
s = 0
l, r = 0, 0
ans = 0
while True:
    if s < K:
        if r == N:
            break
        s += a[ r ]
        r += 1
    else:
        ans += N - r + 1
        s -= a[ l ]
        l += 1

print( ans )