n = int( input() )
l = list( map( int, input().split() ) )

cnt = 0
for i in range( n ):
    li = l[ i ]
    for j in range( i + 1, n ):
        lj = l[ j ]
        for k in range( j + 1, n ):
            lk = l[ k ]
            if ( li - lj ) * ( lj - lk ) * ( lk - li ) == 0:
                continue
            if li + lj > lk and lj + lk > li and lk + li > lj:
                cnt += 1

print( cnt )