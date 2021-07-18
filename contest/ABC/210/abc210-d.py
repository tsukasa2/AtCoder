H, W, C = map( int, input().split() )
A = [ list( map( int, input().split() ) ) for _ in range( H ) ]

ans = 10 ** 18
for h in range( H ):
    for w in range( W ):
        horizonal = []
        for i in range( H ):
            if not i == h:
                horizonal.append( A[ i ][ w ] + C * abs( i - h ) )

        horizonal.sort()
        vertical = []
        for j in range( W ):
            if not j == w:
                vertical.append( A[ h ][ j ] + C * abs( j - w ) )
        
        vertical.sort()
        ans = min(
            [
                ans,
                horizonal[ 0 ] + vertical[ 0 ],
                A[ h ][ w ] + horizonal[ 0 ],
                A[ h ][ w ] + vertical[ 0 ]
            ]
        )

print( ans )