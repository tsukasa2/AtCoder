N = int( input() )
x = list( map( int, input().split() ) )

a, b, c = 0, 0, 0

for i in range( N ):
    a += abs( x[ i ] )
    b += x[ i ] ** 2
    c = max( c, abs( x[ i ] ) )

b = pow( b, 1/2 )

print( a )
print( b )
print( c )