N = int( input() )
a = list( map( int, input().split() ) )

xor_a = 0
for i in range( N ):
    xor_a = xor_a ^ a[ i ]

ans = []
for i in range( N ):
    ans.append( str( xor_a ^ a[ i ] ) )

print( " ".join( ans ) )