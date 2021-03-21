n = int( input() )
x = []
y = []
for _ in range( n ):
    x_k, y_k = map( int, input().split() )
    x.append( x_k )
    y.append( y_k )



# x_max, x_min, y_max, y_min = x[ 0 ], x[ 0 ], y[ 0 ], y[ 0 ]
# for i in range( n ):
#     if x[ i ] > x_max:
#         x_max = x[ i ]
#     if x[ i ] < x_min:
#         x_min = x[ i ]
#     if y[ i ] > y_max:
#         y_max = y[ i ]
#     if y[ i ] < y_min:
#         y_min = y[ i ]
    
# # print( x_max, x_min, y_max, y_min )

# right, top, left, bottom = [], [], [], []
# for i in range( n ):
#     if x[ i ] == x_max:
#         right.append( y[ i ] )
#     if y[ i ] == y_max:
#         top.append( x[ i ] )
#     if x[ i ] == x_min:
#         left.append( y[ i ] )
#     if y[ i ] == y_min:
#         bottom.append( x[ i ] )

# ver = [ ( 0, 0 ) for _ in range( 8 ) ]

# ver[ 0 ] = ( x_max, max( right ) )
# ver[ 1 ] = ( max( top ), y_max )
# ver[ 2 ] = ( min( top ), y_max )
# ver[ 3 ] = ( x_min, max( left ) )
# ver[ 4 ] = ( x_min, min( left ) )
# ver[ 5 ] = ( y_min, min( bottom ) )
# ver[ 6 ] = ( y_min, max( bottom ) )
# ver[ 7 ] = ( x_max, min( right ) )

# max_length = 0
# for i in range( 8 ):
#     for j in range( 8 ):
#         length = abs( ver[ i ][ 0 ] - ver[ j ][ 0 ] ) + abs( ver[ i ][ 1 ] - ver[ j ][ 1 ] )
#         if length > max_length:
#             max_length = length
#             # print( ver[ i ], ver[ j ], length )

# # print( ver )
# print( max_length )