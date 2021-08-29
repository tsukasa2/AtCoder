S = str( input() )

count = [ 0, 0 ]
for d in S:
    count[ int( d ) ] += 1

print( 2 * min( count ) )