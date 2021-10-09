N = str( input() )

numbers = [ int( d ) for d in N ]
numbers.sort( reverse = True )

x = "0"
y = "0"
for n in numbers:
    if int( x ) > int( y ):
        y += str( n )
    else:
        x += str( n )

print( int( x ) * int( y ) )