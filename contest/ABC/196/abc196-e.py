N = int( input() )
a_t = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]
Q = int( input() )
x = list( map( int, input().split() ) )

l = - 10 ** 9
r = 10 ** 9
f_0 = 0
for ( a, t ) in a_t:
    if t == 1:
        l += a
        r += a
        f_0 += a
    elif t == 2:
        l = max( l, a )
        f_0 = max( f_0, a )
    else:
        r = min( r, a )
        f_0 = min( f_0, a )

for x_i in x:
    x_i += f_0
    if x_i < l:
        print( l )
    elif x_i > r:
        print( r )
    else:
        print( x_i )