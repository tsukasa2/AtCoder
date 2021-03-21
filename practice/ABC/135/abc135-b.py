N = int( input() )
p = list( map( int, input().split() ) )

q = sorted( p )
diff = 0
for i in range( N ):
    if not p[ i ] == q[ i ]:
        diff += 1
    if diff > 2:
        print( "NO" )
        break
else:
    print( "YES" )