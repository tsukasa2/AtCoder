N = int( input() )
A = []
x = []
y = []
for _ in range( N ):
    A_i = int( input() )
    A.append( A_i )
    x_i = []
    y_i = []
    for _ in range( A_i ):
        x_ij, y_ij = map( int, input().split() )
        x_i.append( x_ij )
        y_i.append( y_ij )
    x.append( x_i )
    y.append( y_i )

