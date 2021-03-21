n, m = map( int, input().split() )
a = list( map( int, input().split() ) )

def f( a_k ): # 2で割り切れる回数
    count = 0
    while a_k % 2 == 0:
        count += 1
        a_k = a_k // 2
    return count

b = []
f_0 = f( a[ 0 ] )
for a_k in a:
    f_k = f( a_k )
    if f_k != f_0:
        print( 0 )
        exit()
    b.append( a_k // pow( 2, f_k ) )

import math
def lcm( x, y ):
    return x * y // math.gcd( x, y )

b_lcm = 1
for b_k in b:
    b_lcm = lcm( b_lcm, b_k )

a_lcm = b_lcm * pow( 2, f_0 )
# print( b_lcm, f_0, b )
print( ( m + a_lcm // 2 ) // a_lcm )

# import math
# def lcm( x, y ):
#     return x * y // math.gcd( x, y )

# def half_lcm( x, y, m ):
#     r = x // 2
#     while r <= m:
#         print( r, x, y, m )
#         if ( r - y // 2 ) % y == 0:
#             return r
#         r += x
#     return -1

# print( half_lcm( 2, 6, 100 ) )

# if n == 1:
#     print( a[ 0 ] )
# else:
#     preliminary_lcm = lcm( a[ 0 ], a[ 1 ] )
#     preliminary_h_lcm = half_lcm( a[ 0 ], a[ 1 ], m )
#     for i in range( 2, n ):
