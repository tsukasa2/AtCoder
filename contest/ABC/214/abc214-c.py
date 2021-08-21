N = int( input() )
S = list( map( int, input().split() ) )
T = list( map( int, input().split() ) )

sorted_T = sorted( [ ( t, i ) for i, t in enumerate( T ) ] )
_, start = sorted_T[ 0 ]

ans = [ -1 ] * N
ans[ start ] = T[ start ]
for i in range( 1, N ):
    snuke = ( start + i ) % N
    ans[ snuke ] = min( 
        T[ snuke ],
        ans[ ( snuke - 1 ) % N ] + S[ ( snuke - 1 ) % N ]
    )

print( *ans, sep = "\n" )