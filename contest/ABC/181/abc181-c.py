N = int( input() )
x, y = [], []
for _ in range( N ):
    x_i, y_i = map( int, input().split() )
    x.append( x_i )
    y.append( y_i )

def judge( p_1, p_2, p_3 ):
    ( x_1, y_1 ), ( x_2, y_2 ), ( x_3, y_3 ) = p_1, p_2, p_3
    if ( y_2 - y_1 ) * ( x_3 - x_1 ) == ( y_3 - y_1 ) * ( x_2 - x_1 ):
        return True
    else:
        return False

flag = False
for i in range( N - 2 ):
    for j in range( i + 1, N - 1 ):
        for k in range( j + 1, N ):
            p_i, p_j, p_k = ( x[ i ], y[ i ] ), ( x[ j ], y[ j ] ), ( x[ k ], y[ k ] )
            if judge( p_i, p_j, p_k ) == True:
                flag = True

if flag == True:
    print( "Yes" )
else:
    print( "No" )