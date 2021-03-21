n = int( input() )
a = list( map( int, input().split() ) )
a = [ a[-1] ] + a + [ a[0] ]

x = [ 0 ] * ( n+1 )

for i in range( 1, n+1 ):
    x[n] = x[n] + a[i]

for k in range( 1, n//2+1 ):
    x[n] = x[n] - 2*a[ 2*k - 1 ]

for i in reversed( range( 1, n ) ):
    x[i] = 2*a[i] - x[i+1]

x = list( map( str, x ) )

print( " ".join( x[1:n+1] ) )