N = int( input() )
a_t = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]
Q = int( input() )
x = list( map( int, input().split() ) )

def F( x ):
    # F( x ) = f_N( ... f_2( f_1( x ) ) ... )
    y = x

    for ( a, t ) in a_t:
        if t == 1:
            y = y + a
        elif t == 2:
            y = max( y, a )
        else:
            y = min( y, a )
    
    return y

# F( x ) =
#     y_2 ( x > x_2のとき )
#     x ( x_1 <= x <= x_2のとき )
#     y_1 ( x < x_1のとき )
# となる．x_1，x_2，y_1，y_2を求める
y_2 = F( 10 ** 9 )
y_1 = F( - 10 ** 9 )

# 二分探索でx_2を求める
l = - 10 ** 9
r = 10 ** 9
while r - l > 1:
    m = ( l + r ) // 2
    y = F( m )
    if y < y_2:
        l = m
    else:
        r = m

x_2 = r

# 二分探索でx_1を求める
l = - 10 ** 9
r = 10 ** 9
while r - l > 1:
    m = ( l + r ) // 2
    y = F( m )
    if y > y_1:
        r = m
    else:
        l = m

x_1 = l

for x_i in x:
    if x_i < x_1:
        print( y_1 )
    elif x_i < x_2:
        print( ( y_2 - y_1 ) * ( x_i - x_1 ) // ( x_2 - x_1 ) + y_1 )
    else:
        print( y_2 )
    