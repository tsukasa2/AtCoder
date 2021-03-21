N, K = map( int, input().split() )
h = list( map( int, input().split() ) )

h.sort()
h.append( K )

i = 0
while h[ i ] < K:
    i += 1

print( N - i )