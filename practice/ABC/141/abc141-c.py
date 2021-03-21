N, K, Q = map( int, input().split() )
A = [ int( input() ) - 1 for _ in range( Q ) ]

score = [ K for _ in range( N ) ]

for a in A:
    score[ a ] += 1

for i in range( N ):
    if score[ i ] - Q > 0:
        print( "Yes" )
    else:
        print( "No" )