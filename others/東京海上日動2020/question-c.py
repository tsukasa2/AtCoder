n, k = map( int, input().split() )
a = list( map( int, input().split() ) )

# 以下カンニング
for _ in range( min( k, 41 ) ): # 41 ~ log( 2 * 10 ** 5 )
    b = [ 0 ] * n

    for i in range( n ):
        l = max( 0, i - a[ i ] )
        r = min( n - 1, i + a[ i ] )
        b[ l ] += 1
        if r + 1 < n:
            b[ r + 1 ] -= 1

    for i in range( 1, n ):
        b[ i ] += b[ i - 1 ]

    a = b

print( " ".join( list( map( str, a ) ) ) )