N = int( input() )
A = list( map( int, input().split() ) )

b = [ 0 for _ in range( 30 ) ]
for a in A:
    bin_a = bin( a )[ 2: ]
    for i in range( len( bin_a ) ):
        if bin_a[ i ] == "1":
            b[ i ] += 1

ans = 0
for i in range( 30 ):
    if b [ i ] == 1:
        ans += 2 ** i

print( ans )