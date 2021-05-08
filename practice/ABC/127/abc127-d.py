N, M = map( int, input().split() )
A = list( map( int, input().split() ) )
BC = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

CB = [ ( C, B ) for ( B, C ) in BC ]
A.sort()
CB.sort( reverse = True )

i = 0
for ( C, B ) in CB:
    for _ in range( B ):
        if A[ i ] < C:
            A[ i ] = C
            i += 1
            if i > N - 1:
                break
        else:
            break
    else:
        continue

    break

print( sum( A ) )