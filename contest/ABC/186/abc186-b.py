H, W = map( int, input().split() )
A = []
for _ in range( H ):
    a = list( map( int, input().split() ) )
    # A.append( a )
    A += a

base = min( A )
print( sum( A ) - base * H * W )