# n = int( input() )
# a = list( map( int, input().split() ) )

# a.sort()
# p = []
# k = set()

# while a:
#     prime = a[ 0 ]

#     p.append( prime )

#     i = 0
#     flag = 0
#     while i < len( a ):
#         if a[ i ] == prime and flag == 1:
#             k.add( prime )
#         flag = 1
#         if a[ i ] % prime == 0:
#             a.pop( i )
#             continue
#         i += 1

# print( p, k )
# print( len( p ) - len( k ) 

# 以下カンニング
n = int( input() )
a = list( map( int, input().split() ) )

max_a = max( a )

c = {} # c[ a_i ] = aに含まれるa_iの個数
d = {} # d[ a_i ] = aにa_iの約数( < a_i )があるか(bool)
for a_i in a:
    try:
        c[ a_i ] += 1
    except KeyError:
        c[ a_i ] = 1
        d[ a_i ] = False # 初期値

for a_i in a:
    if c[ a_i ] > 0:
        tmp = 2 * a_i
        while tmp <= max_a:
            d[ tmp ] = True
            tmp += a_i

ans = 0
for a_i in a:
    if c[ a_i ] == 1 and d[ a_i ] == False:
        ans += 1

print( ans )
