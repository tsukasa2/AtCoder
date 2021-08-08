N, M = map( int, input().split() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )

AtB = []
for a in A:
    AtB.append( ( a, "A" ) )

for b in B:
    AtB.append( ( b, "B" ) )

AtB.sort()
ans = 10 ** 9 + 100
for i in range( N + M - 1 ):
    x = AtB[ i ]
    y = AtB[ i + 1 ]
    if not x[ 1 ] == y[ 1 ]:
        ans = min( ans, y[ 0 ] - x[ 0 ] )

print( ans )