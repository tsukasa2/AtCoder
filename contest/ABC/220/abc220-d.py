N = int( input() )
A = list( map( int, input().split() ) )
MOD = 998244353

DP = [ [ 0 ] * 10 for _ in range( N ) ]
# DP[ i ][ j ] = ちょうどi回の操作で左端をjにする手順の数

DP[ 0 ][ A[ 0 ] ] = 1
for i in range( N - 1 ):
    y = A[ i + 1 ]
    for j in range( 10 ):
        DP[ i + 1 ][ ( j + y ) % 10 ] += DP[ i ][ j ]
        DP[ i + 1 ][ ( j + y ) % 10 ] %= MOD
        DP[ i + 1 ][ ( j * y ) % 10 ] += DP[ i ][ j ]
        DP[ i + 1 ][ ( j * y ) % 10 ] %= MOD

print( *DP[ -1 ], sep = "\n" )