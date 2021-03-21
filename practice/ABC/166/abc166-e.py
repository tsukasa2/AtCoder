N = int( input() )
A = list( map( int, input().split() ) )

count = {}
for i in range( 1, N + 1 ):
    try:
        count[ i + A[ i - 1 ] ] += 1
    except KeyError:
        count[ i + A[ i - 1 ] ] = 1

ans = 0
for i in range( 1, N + 1 ):
    try:
        ans += count[ i - A[ i - 1 ] ]
    except KeyError:
        continue

print( ans )