n = int( input() )
x = []
y = []
p = []
for _ in range( n ):
    x_i, y_i, p_i = map( int, input().split() )
    if x_i == 0 or y_i == 0:
        p_i = 0
    x.append( x_i )
    y.append( y_i )
    p.append( p_i )

rail_h = [ 0 ]
rail_v = [ 0 ]

def nearest( city, r_v, r_h ):
    nearest_x = [ abs( v - x[ city ] ) for v in r_v ]
    nearest_y = [ abs( h - y[ city ] ) for h in r_h ]
    return min( min( nearest_x ), min( nearest_y ) )

def sum_steps():
    min_s = float( "Inf" )
    min_xy = 0
    pm = 0
    for x_i in x:
        s_i = 0
        for i in range( n ):
            d = nearest( i, rail_v + [ x_i ], rail_h )
            s_i += d * p[ i ]
        if min_s > s_i:
            min_s = s_i
            min_xy = x_i
            pm = 1
    for y_i in y:
        s_i = 0
        for i in range( n ):
            d = nearest( i, rail_v, rail_h + [ y_i ] )
            s_i += d * p[ i ]
        if min_s > s_i:
            min_s = s_i
            min_xy = y_i
            pm = -1
    return min_s, min_xy, pm

s = 0
for i in range( n ):
    d = nearest( i, rail_v, rail_h )
    s += d * p[ i ]
    if d == 0:
        p[ i ] = 0
print( s )

for k in range( n ):
    s = 0
    s_i, xy_i, pm = sum_steps()
    s += s_i
    print( s )

    if pm > 0:
        rail_v.append( xy_i )
        for i in range( n ):
            if x[ i ] == xy_i:
                p[ i ] = 0
    else:
        rail_h.append( xy_i )
        for i in range( n ):
            if y[ i ] == xy_i:
                p[ i ] = 0

