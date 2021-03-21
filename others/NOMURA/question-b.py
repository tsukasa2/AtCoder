t = str( input() )
n = len( t )
s = []
for i in range( n ):
    if t[ i ] == "P":
        s.append( "P" )
    else:
        s.append( "D" )
print( "".join( s ) )