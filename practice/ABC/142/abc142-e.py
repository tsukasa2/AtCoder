N, M = map( int, input().split() )
a, b, c = [], [], []
for _ in range( M ):
    a_i, b_i = map( int, input().split() )
    c_i_list = list( map( int, input().split() ) )
    a.append( a_i )
    b.append( b_i )
    c_i = 0
    for d in c_i_list:
        c_i += 2 ** ( d - 1 )
    c.append( c_i )

INF = 10 ** 8
dp = [ [ INF for _ in range( 2 ** N ) ] for _ in range( M + 1 ) ]
# dp[ i ][ S ] = 鍵が最初のi個しかないときの，
#   集合Sに含まれる宝箱を開けるための最小コスト
dp[ 0 ][ 0 ] = 0

for i in range( M ):
    for S in range( 2 ** N ):
        if dp[ i + 1 ][ S ] > dp[ i ][ S ]:
            dp[ i + 1 ][ S ] = dp[ i ][ S ]
        if dp[ i + 1 ][ S | c[ i ] ] > dp[ i ][ S ] + a[ i ]:
            dp[ i + 1 ][ S | c[ i ] ] = dp[ i ][ S ] + a[ i ]

if dp[ M ][ 2 ** N - 1 ] < INF:
    print( dp[ M ][ 2 ** N - 1 ] )
else:
    print( -1 )