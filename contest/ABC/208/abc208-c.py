N, K = map( int, input().split() )
a = list( map( int, input().split() ) )

ans = [ 0 for _ in range( N ) ]

a_i = [ ( a[ i ], i ) for i in range( N ) ]
a_i.sort()

q = K // N
r = K % N
for i in range( N ):
    x, y = a_i[ i ]
    if i < r:
        ans[ y ] = q + 1
    else:
        ans[ y ] = q

for an in ans:
    print( an )