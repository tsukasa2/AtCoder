n = int( input() )

n_list = [ 0 for _ in range( 10 ** 4 + 1 ) ]

def g( x, y, z ):
    return min( x * x + y * y + z * z + x * y + y * z + z * x, 10 ** 4 + 1 )

for x in range( 1, 101 ):
    for y in range( 1, 101 ):
        for z in range( 1, 101 ):
            n_list[ g( x, y, z ) - 1 ] += 1

for k in range( n ):
    print( n_list[ k ] )