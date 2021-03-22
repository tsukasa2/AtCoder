N = int( input() )
C = [ list( map( int, input().split() ) ) for _ in range( N ) ]

min_line = -1
min_sum = N * ( 10 ** 9 ) + 100

for i in range( N ):
    sum_i = sum( C[ i ] )
    if sum_i < min_sum:
        min_line = i
        min_sum = sum_i

B = C[ min_line ]
A = []
for i in range( N ):
    A.append( C[ i ][ 0 ] - B[ 0 ] )

for i in range( N ):
    for j in range( N ):
        if C[ i ][ j ] - B[ j ] != A[ i ]:
            print( "No" )
            exit()

print( "Yes" )
print( " ".join( map( str, A ) ) )
print( " ".join( map( str, B ) ) )