N, K = map( int, input().split() )
A = list( map( int, input().split() ) )

A.sort( reverse = True )

DP = [ 0 ] * N
DP[ 0 ] = K
for i in range( 1, N ):
    DP[ i ] = max( 0, DP[ i - 1 ] - ( A[ i - 1 ] - A[ i ] ) * i )

for i in range( N - 1 ):
    DP[ i ] -= DP[ i + 1 ]

# print( DP )
ans = 0
for i in range( N ):
    x = DP[ i ] // ( i + 1 )
    y = DP[ i ] % ( i + 1 )
    if x > A[ i ]:
        x = A[ i ]
        y = 0

    ans += ( ( A[ i ] + ( A[ i ] - x + 1 ) ) * x // 2 ) * ( i + 1 )
    ans += ( A[ i ] - x ) * y

print( ans )