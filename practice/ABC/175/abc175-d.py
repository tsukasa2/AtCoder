N, K = map( int, input().split() )
P = list( map( int, input().split() ) )
C = list( map( int, input().split() ) )

P = [ p - 1 for p in P ]

from collections import deque
queue = deque( [ i for i in range( N ) ] )
visited = [ False for _ in range( N ) ]
loops = []
loop = []
while queue:
    v = queue.popleft()
    if visited[ v ] == True:
        continue

    visited[ v ] = True
    loop.append( C[ v ] )

    u = P[ v ]
    if visited[ u ] == False:
        queue.appendleft( u )
    else:
        loops.append( loop )
        loop = []

# print( loops )

ans = - 10 ** 9 - 1000

for loop in loops:
    for i in range( 1, min( K, len( loop ) ) + 1 ):
        r = - 10 ** 9 - 1000
        l = 10 ** 18
        r_i = sum( loop[ : i ] )
        for j in range( len( loop ) ):
            r_i = r_i - loop[ j ] + loop[ ( j + i ) % len( loop ) ]
            if r_i > r:
                # print( i, j, r_i, r, l )
                r = r_i
                l = i
    
        if sum( loop ) > 0:
            r += sum( loop ) * ( ( K - l ) // len( loop ) )
        # print( loop, r )
        ans = max( ans, r )

print( ans )