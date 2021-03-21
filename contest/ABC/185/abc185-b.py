N, M, T = map( int, input().split() )
A, B = [], []
for _ in range( M ):
    A_i, B_i = map( int, input().split() )
    A.append( A_i )
    B.append( B_i )

flag = True
battery = N - A[ 0 ]

if battery <= 0:
    flag = False

battery += B[ 0 ] - A[ 0 ]
battery = min( battery, N )

for i in range( 1, M ):
    battery -= A[ i ] - B[ i - 1 ]
    if battery <= 0:
        flag = False
    battery += B[ i ] - A[ i ]
    battery = min( battery, N )

battery -= T - B[ -1 ]
if battery <= 0:
    flag = False

if flag == True:
    print( "Yes" )
else:
    print( "No" )