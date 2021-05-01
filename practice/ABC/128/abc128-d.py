from collections import deque

N, K = map( int, input().split() )
V = list( map( int, input().split() ) )

ans = -1
for k in range( K + 1 ):
    for pick in range( min( k + 1, N + 1 ) ):
        for a in range( pick + 1 ):
            hand = []
            if a > 0:
                hand += V[ : a ]
            
            if pick - a > 0:
                hand += V[ - min( pick - a, N - a ) : ]
        
            hand.sort()
            score = sum( hand[ k - pick : ] )
            ans = max( ans, score )
            # print( k, pick, a, score, hand[ k - pick : ] )

print( ans )