N = int( input() )
A, B = [], []
for _ in range( N ):
    A_i, B_i = map( int, input().split() )
    A.append( A_i )
    B.append( B_i )

ans = 0
for i in range( N ):
    ans += ( A[ i ] + B[ i ] ) * ( B[ i ] - A[ i ] + 1 ) // 2

print( ans )