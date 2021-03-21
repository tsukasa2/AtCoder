import itertools

N, K = map( int, input().split() )
T = []
for _ in range( N ):
    T_i = list( map( int, input().split() ) )
    T.append( T_i )

town = [ i for i in range( N ) ]
ans = 0
for p in itertools.permutations( town[ 1: ], N - 1 ):
    time = 0
    town_p = 0
    for i in p:
        time += T[ town_p ][ i ]
        town_p = i
    time += T[ town_p ][ 0 ]
    if time == K:
        ans += 1

print( ans )