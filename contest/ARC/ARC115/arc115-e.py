N = int( input() )
A = list( map( int, input().split() ) )
MOD = 998244353

X = []
X.append( [ A[ 0 ] - max( A[ 0 ] - A[ 1 ], 0 ), max( A[ 0 ] - A[ 1 ], 0 ) ] )

for i in range( 1, N - 1 ):
    a = A[ i ] - max( A[ i ] - A[ i + 1 ], 0 )
    b = max( A[ i ] - A[ i + 1 ], 0 )

    c = X[ i - 1 ][ 0 ] * ( a - 1 ) + X[ i - 1 ][ 1 ] * a
    d = X[ i - 1 ][ 0 ] * ( b - 1 ) + X[ i - 1 ][ 1 ] * b
    c %= MOD
    d %= MOD
    X.append( [ c, d ] )

a = A[ N - 1 ]
b = 0

c = X[ N - 1 - 1 ][ 0 ] * ( a - 1 ) + X[ N - 1 - 1 ][ 1 ] * a
d = X[ N - 1 - 1 ][ 0 ] * ( b - 1 ) + X[ N - 1 - 1 ][ 1 ] * b
c %= MOD
d %= MOD
X.append( [ c, d ] )

print( X )
print( ( X[ -1 ][ 0 ] + X[ -1 ][ 1 ] ) % MOD )