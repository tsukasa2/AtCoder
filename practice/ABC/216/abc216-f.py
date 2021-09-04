N = int( input() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )
MOD = 998244353

C = [ ( A[ i ], B[ i ] ) for i in range( N ) ]
C.sort()

A = [ a for a, _ in C ]
B = [ b for _, b in C ]

A_max = max( A )

f = [ [ 0 ] * ( A_max + 1 ) for _ in range( N + 1 ) ]
# f[ i ][ j ] = B_1 ~ B_iから和がjになるように選ぶ方法の数

f[ 0 ][ 0 ] = 1
for i in range( 1, N + 1 ):
    for j in range( A_max + 1 ):
        if B[ i - 1 ] <= j:
            f[ i ][ j ] += f[ i - 1 ][ j - B[ i - 1 ] ]
        
        f[ i ][ j ] += f[ i - 1 ][ j ]
        f[ i ][ j ] %= MOD
# print( *f, sep = "\n" )
ans = 0
for i in range( 1, N + 1 ):
    for j in range( A[ i - 1 ] - B[ i - 1 ] + 1 ):
        ans += f[ i - 1 ][ j ]
        ans %= MOD

print( ans )