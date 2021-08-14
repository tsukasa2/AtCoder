H, W, N = map( int, input().split() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

X, Y = [], []
i = 0
for a, b in AB:
    X.append( ( a, i ) )
    Y.append( ( b, i ) )
    i += 1

X.sort()
Y.sort()

ans = [ [ 0, 0 ] for _ in range( N ) ]
j = 0
p = -1
for a, i in X:
    if not a == p:
        j += 1
        p = a
    ans[ i ][ 0 ] = j

j = 0
p = -1
for b, i in Y:
    if not b == p:
        j += 1
        p = b
    ans[ i ][ 1 ] = j

for a, b in ans:
    print( a, b )