N, X = map( int, input().split() )
L = list( map( int, input().split() ) )

D = 0
ans = 1
for l in L:
    if D + l > X:
        break
    else:
        D += l
        ans += 1

print( ans )