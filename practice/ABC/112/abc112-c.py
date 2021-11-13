N = int( input() )
xyh = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

xyh.sort( key = lambda x: x[ 2 ] )
x_0, y_0, h_0 = xyh[ -1 ]

def calc_H( c_x, c_y ):
    return h_0 + abs( x_0 - c_x ) + abs( y_0 - c_y )

def calc_h( x, y, c_x, c_y, H ):
    return max(
        H - abs( x - c_x ) - abs( y - c_y ),
        0
    )

for c_x in range( 101 ):
    for c_y in range( 101 ):
        H = calc_H( c_x, c_y )
        flag = True
        for x, y, h in xyh:
            if not h == calc_h( x, y, c_x, c_y, H ):
                flag = False
            
        if flag == True:
            print( c_x, c_y, H )
            exit()