import array
from bisect import bisect_left, insort_left

A, B, Q = map( int, input().split() )
s = [ int( input() ) for _ in range( A ) ]
t = [ int( input() ) for _ in range( B ) ]
x = [ int( input() ) for _ in range( Q ) ]

s_tree = array.array( "L", [] )
t_tree = array.array( "L", [] )
for s_i in s:
    insort_left( s_tree, s_i )

for t_i in t:
    insort_left( t_tree, t_i )

for x_i in x:
    index_s = bisect_left( s_tree, x_i )
    index_t = bisect_left( t_tree, x_i )
    
    if index_s == 0:
        s_l = -10 ** 18
    else:
        s_l = s_tree[ index_s - 1 ]
    
    if index_t == 0:
        t_l = -10 ** 18
    else:
        t_l = t_tree[ index_t - 1 ]
    
    if index_s == A:
        s_r = 10 ** 18
    else:
        s_r = s_tree[ index_s ]
    
    if index_t == B:
        t_r = 10 ** 18
    else:
        t_r = t_tree[ index_t ]

    # print( x_i, s_l, s_r, t_l, t_r )
    print(
        min(
            [
                max( s_r, t_r ) - x_i,
                x_i - min( s_l, t_l ),
                ( x_i - s_l ) + ( t_r - s_l ),
                ( x_i - t_l ) + ( s_r - t_l ),
                ( s_r - x_i ) + ( s_r - t_l ),
                ( t_r - x_i ) + ( t_r - s_l )
            ]
        )
    )