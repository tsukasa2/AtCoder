N = int( input() )
A = list( map( int, input().split() ) )

S_1 = [ A[ 0 ] ]
for i in range( 1, N ):
    S_1.append( S_1[ -1 ] + A[ i ] )

S_2 = [ A[ 0 ] ** 2 ]
for i in range( 1, N ):
    S_2.append( S_2[ -1 ] + A[ i ] ** 2 )

ans = 0
for i in range( 1, N ):
    ans += i * A[ i ] ** 2
    ans += -2 * A[ i ] * S_1[ i - 1 ]
    ans += S_2[ i - 1 ]

print( ans )