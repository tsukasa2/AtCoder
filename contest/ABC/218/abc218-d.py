N = int( input() )
xy = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

lines = {}
for x_0, y_0 in xy:
    for x_1, y_1 in xy:
        if y_0 == y_1 and x_0 < x_1:
            if x_0 in lines.keys():
                if x_1 - x_0 in lines[ x_0 ].keys():
                    lines[ x_0 ][ x_1 - x_0 ] += 1
                else:
                    lines[ x_0 ][ x_1 - x_0 ] = 1
            else:
                lines[ x_0 ] = { x_1 - x_0 : 1 }

ans = 0
for x in lines.keys():
    for length in lines[ x ].keys():
        c = lines[ x ][ length ]
        ans += c * ( c - 1 ) // 2

print( ans )