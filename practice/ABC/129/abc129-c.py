MOD = 10 ** 9 + 7

N, M = map( int, input().split() )
a = [ int( input() ) for _ in range( M ) ]

is_broken = [ False for _ in range( N ) ]
for a_i in a:
    is_broken[ a_i - 1 ] = True

if N == 1:
    if is_broken[ 0 ] == False:
        print( 1 )
    else:
        print( 0 )
    exit()

DP = [ 0 for _ in range( N ) ]

if is_broken[ 0 ] == False:
    DP[ 0 ] += 1

if is_broken[ 1 ] == False:
    DP[ 1 ] += DP[ 0 ] + 1

for i in range( N - 2 ):
    if is_broken[ i + 2 ] == False:
        DP[ i + 2 ] += DP[ i ] + DP[ i + 1 ]
        DP[ i + 2 ] %= MOD

print( DP[ N - 1 ] )