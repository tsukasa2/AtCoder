r, D, x_2000 = map( int, input().split() )

x_i = x_2000
for i in range( 10 ):
    x_i = r * x_i - D
    print( x_i )