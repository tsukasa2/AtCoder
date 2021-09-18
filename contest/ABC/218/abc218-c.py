N = int( input() )
S = [ str( input() ) for _ in range( N ) ]
T = [ str( input() ) for _ in range( N ) ]

x_min, x_max = N + 1, -1
y_min, y_max = N + 1, -1
for x in range( N ):
    for y in range( N ):
        if S[ x ][ y ] == "#":
            x_min = min( x_min, x )
            x_max = max( x_max, x )
            y_min = min( y_min, y )
            y_max = max( y_max, y )

s = []
for x in range( x_max - x_min + 1 ):
    s_i = ""
    for y in range( y_max - y_min + 1 ):
        s_i += S[ x + x_min ][ y + y_min ]
    
    s.append( s_i )

x_min, x_max = N + 1, -1
y_min, y_max = N + 1, -1
for x in range( N ):
    for y in range( N ):
        if T[ x ][ y ] == "#":
            x_min = min( x_min, x )
            x_max = max( x_max, x )
            y_min = min( y_min, y )
            y_max = max( y_max, y )

t = []
for x in range( x_max - x_min + 1 ):
    t_i = ""
    for y in range( y_max - y_min + 1 ):
        t_i += T[ x + x_min ][ y + y_min ]
    
    t.append( t_i )

# print( s, sep = "\n" )
# print( t, sep = "\n" )

if len( s ) == len( t ) and len( s[ 0 ] ) == len( t[ 0 ] ):
    w = len( s )
    h = len( s[ 0 ] )
    for x in range( w ):
        flag = True
        for y in range( h ):
            if not s[ x ][ y ] == t[ x ][ y ]:
                flag = False
        if flag == False:
            break
    else:
        print( "Yes" )
        exit()
    
    for x in range( w ):
        flag = True
        for y in range( h ):
            if not s[ -x - 1 ][ -y - 1 ] == t[ x ][ y ]:
                flag = False
        if flag == False:
            break
    else:
        print( "Yes" )
        exit()

if len( s[ 0 ] ) == len( t ) and len( s ) == len( t[ 0 ] ):
    w = len( s )
    h = len( s[ 0 ] )
    for x in range( w ):
        flag = True
        for y in range( h ):
            if not s[ x ][ y ] == t[ -y - 1 ][ x ]:
                flag = False
        if flag == False:
            break
    else:
        print( "Yes" )
        exit()
    
    for x in range( w ):
        flag = True
        for y in range( h ):
            if not s[ -x - 1 ][ -y - 1 ] == t[ -y - 1 ][ x ]:
                flag = False
        if flag == False:
            break
    else:
        print( "Yes" )
        exit()

print( "No" )