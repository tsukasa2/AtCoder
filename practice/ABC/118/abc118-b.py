N, M = map( int, input().split() )
K, A = [], []
for _ in range( N ):
    ka = list( map( int, input().split() ) )
    K.append( ka[ 0 ] )
    A.append( ka[ 1 : ] )

count = [ 0 ] * M
for a_i in A:
    for a_ij in a_i:
        count[ a_ij - 1 ] += 1
    
ans = 0
for c in count:
    if c == N:
        ans += 1

print( ans )