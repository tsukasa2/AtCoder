n, a, b = map( int, input().split() )
m = n // ( a + b )
p = n % ( a + b )
print( m * a + min( p, a ) )