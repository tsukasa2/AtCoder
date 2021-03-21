n = int( input() )
d_1 = []
d_2 = []
for _ in range( n ):
    a, b = map( int, input().split() )
    d_1.append( a )
    d_2.append( b )

for i in range( n - 2 ):
    if d_1[ i ] == d_2[ i ] and d_1[ i + 1 ] == d_2[ i + 1 ] and d_1[ i + 2 ] == d_2[ i + 2 ]:
        print( "Yes" )
        break
else:
    print( "No" )