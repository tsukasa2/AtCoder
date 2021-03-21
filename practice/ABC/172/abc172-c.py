N, M, K = map( int, input().split() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )

time = 0
l = 0
while True:
    if l >= N:
        break
    if time + A[ l ] > K:
        break
    time += A[ l ]
    l += 1

r = 0
ans = 0
while True:
    while True:
        if r >= M:
            break
        if time + B[ r ] > K:
            break
        time += B[ r ]
        r += 1
    
    # print( "( time, l, r ):", time, l, r )
    
    if ans < l + r:
        ans = l + r
        # print( "ans is updated" )
    
    if r >= M - 1 or l <= 0:
        break

    while True:
        time -= A[ l - 1 ]
        l -= 1
        if time < K or l <= 0:
            break

print( ans )