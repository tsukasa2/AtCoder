# 復習
N, Q = map( int, input().split() )
C = list( map( int, input().split() ) )
Query = []
for _ in range( Q ):
    Query_i = tuple( map( int, input().split() ) )
    Query.append( Query )

group = [ -1 for _ in range( N ) ]
# group[ i ] = 生徒iを含む集団の親 or 生徒iが親を務める集団の人数の-1倍
member = [ [ i ] for i in range( N ) ]
# member[ i ] = 生徒iが親を務める集団のメンバー

for q in Query:
    if q[ 0 ] == 1:
        a = q[ 1 ] - 1
        b = q[ 2 ] - 1
        
        if group[ a ] < 0:
            p_a = a
        else:
            p_a = group[ a ]
        
        if group[ b ] < 0:
            p_b = b
        else:
            p_b = group[ b ]

        if -group[ p_a ] < -group[ p_b ]:
            a, b = b, a
            p_a, p_b = p_b, p_a

        group[ p_a ] += group[ p_b ]
        for m in member[ p_b ]:
            group[ m ] = p_a
            member[ p_a ].append( m )
    else:
        
        

