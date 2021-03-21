n, k = map( int, input().split() )
a = [ 0 ] + list( map( int, input().split() ) )

now = 1
visited = [ 1, -1 ] + [ -1 ] * ( n - 1 )
diary = [ -1, 0 ] + [ -1 ] * ( n - 1 )

for i in range( 1, k+1 ):
    now = a[ now ]
    visited[ i ] = now
    if diary[ now ] != -1:
        cycle = i - diary[ now ]
        d = ( k - i ) % cycle
        now = visited[ diary[ now ] + d ]
        break
    else:
        diary[ now ] = i

print( now )