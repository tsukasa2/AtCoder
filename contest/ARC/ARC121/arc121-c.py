T = int( input() )
for _ in range( T ):
    N = int( input() )
    p = list( map( int, input().split() ) )

    ans = []

    index_p = [ -1 for _ in range( N + 1 ) ]
    for ( i, p_i ) in enumerate( p ):
        index_p[ p_i ] = i
    
    # 1を正しい位置に移動
    if index_p[ 1 ] > 1 and index_p[ 1 ] % 2 == 0:
        p[ 0 ], p[ 1 ] = p[ 1 ], p[ 0 ]
        index_p[ p[ 0 ] ], index_p[ p[ 1 ] ] = index_p[ p[ 1 ] ], index_p[ p[ 0 ] ]

    while index_p[ 1 ] > 0:
        i = index_p[ 1 ]
        p[ i - 1 ], p[ i ] = p[ i ], p[ i - 1 ]
        index_p[ p[ i - 1 ] ], index_p[ p[ i ] ] = index_p[ p[ i ] ], index_p[ p[ i - 1 ] ]
        ans.append( ( i - 1 ) + 1 )
    
    # 2を正しい位置に移動
    if index_p[ 2 ] > 2 and index_p[ 1 ] % 2 == 1:
        p[ 1 ], p[ 2 ] = p[ 2 ], p[ 1 ]
        index_p[ p[ 1 ] ], index_p[ p[ 2 ] ] = index_p[ p[ 2 ] ], index_p[ p[ 1 ] ]

    while index_p[ 2 ] > 1:
        i = index_p[ 2 ]
        p[ i - 1 ], p[ i ] = p[ i ], p[ i - 1 ]
        index_p[ p[ i - 1 ] ], index_p[ p[ i ] ] = index_p[ p[ i ] ], index_p[ p[ i - 1 ] ]
        ans.append( ( i - 1 ) + 1 )
    
    one_and_two_are_reversed = False
    for i in range( 3, N + 1 ):
        # iを正しい位置に移動
        if index_p[ i ] > i and index_p[ i ] % 2 != i % 2:
            one_and_two_are_reversed = not one_and_two_are_reversed
            ans.append( 1 )

    while index_p[ 2 ] > 1:
        i = index_p[ 2 ]
        p[ i - 1 ], p[ i ] = p[ i ], p[ i - 1 ]
        index_p[ p[ i - 1 ] ], index_p[ p[ i ] ] = index_p[ p[ i ] ], index_p[ p[ i - 1 ] ]
        ans.append( ( i - 1 ) + 1 )