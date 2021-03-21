N, K = map( int, input().split() )
x = list( map( int, input().split() ) )

# x_minus = [ - ( 10 ** 8 + 1 ) ]
# x_plus = []
# for x_i in x:
#     if x_i >= 0:
#         x_plus.append( x_i )
#     else:
#         x_minus.append( x_i )
# x_plus.append( 10 ** 8 + 1 )

# l, r = -1, 0
# for k in range( K ):
#     if -x_minus[ l ] < x_plus[ r ]:
#         l -= 1
#     else:
#         r += 1

# # print( l, r )

# if l == - ( K + 1 ):
#     print( -x_minus[ -K ] )
# elif r == K:
#     print( x_plus[ K - 1 ] )
# else:
#     if -x_minus[ l + 1 ] < x_plus[ r - 1 ]:
#         print( -x_minus[ l + 1 ] * 2 + x_plus[ r - 1 ] )
#     else:
#         print( x_plus[ r - 1 ] * 2 - x_minus[ l + 1 ] )

def time( x, l, r ):
    if x[ l ] > 0:
        return x[ r ]
    elif x[ r ] < 0:
        return -x[ l ]
    else:
        if -x[ l ] < x[ r ]:
            return -x[ l ] * 2 + x[ r ]
        else:
            return x[ r ] * 2 + ( -x[ l ] )

min_time = time( x, 0, N-1 )
for i in range( N - K + 1 ):
    time_i = time( x, i, i + K - 1 )
    if time_i < min_time:
        min_time = time_i

print( min_time )