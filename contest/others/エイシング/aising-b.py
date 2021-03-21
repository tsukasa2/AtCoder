n = int( input() )
a = list( map( int, input().split() ) )

ans = 0
for k in range( n ):
    if ( k + 1 ) % 2 == 1 and a[ k ] % 2 == 1:
        ans += 1

print( ans )