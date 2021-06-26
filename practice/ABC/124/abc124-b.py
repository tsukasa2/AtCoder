N = int( input() )
H = list( map( int, input().split() ) )

ans = 0
h_max = -1
for h in H:
    if h >= h_max:
        ans += 1
        h_max = h

print( ans )