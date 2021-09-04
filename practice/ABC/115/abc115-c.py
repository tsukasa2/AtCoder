N, K = map( int, input().split() )
h = [ int( input() ) for _ in range( N ) ]

h.sort()

ans = 10 ** 9 + 100
for i in range( N - ( K - 1 ) ):
    h_max = h[ i + K - 1 ]
    h_min = h[ i ]
    ans = min( ans, h_max - h_min )

print( ans )