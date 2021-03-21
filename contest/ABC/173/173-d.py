# n = int( input() )
# a = list( map( int, input().split() ) )
# a.sort()

# a_list = []
# a_dic = {}
# for a_i in reversed( a[ : -2 ] ):
#     try:
#         a_dic[ a_i ] += 1
#     except KeyError:
#         a_dic[ a_i ] = 1
#         a_list.append( a_i )

# ans = a_list[ 0 ]
# for a_i in a_list[1:]:
#     print( ans )
#     ans += ( a_dic[ a_i ] + 1 ) * a_i

# print( ans )

# 以下カンニング
n = int( input() )
a = list( map( int, input().split() ) )
a.sort()

ans = 0
for k in range( 1, n ):
    ans += a[ n - k // 2 - 1]

print( ans )