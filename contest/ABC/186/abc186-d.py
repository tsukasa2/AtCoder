N = int( input() )
A = list( map( int, input().split() ) )

A.sort()
A_s = [ A[ 0 ] ] # A_s[ i ] = A[ 0 ] + A[ 1 ] + ... + A[ i ]
for i in range( 1, N ):
    A_s.append( A_s[ -1 ] + A[ i ] )

ans = 0
for i in range( N ):
    ans += ( A_s[ N - 1 ] - A_s[ i ] ) - A[ i ] * ( N - 1 - i )

print( ans )