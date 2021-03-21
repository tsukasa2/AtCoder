n, x, y = list( map( int, input().split() ) )

# #1,2,...,X,Y,...,N
# def a( k ):
#     ver = n - ( y - 1 ) + x
#     if ver < k:
#         return 0
#     else:
#         return ver - k

# #X+1,X+2,...,Y
# def b( k ):
#     ver = y - ( x - 1 )
#     if k > ver / 2:
#         return 0
#     else:
#         return ver

# #1,2,...,X,X+1,...,Y
# def c( k ):
#     if k < 2 or x == 1:
#         return 0
#     half = ( y - ( x - 1 ) ) // 2
#     scope = min( ( x + k - 1 ), ( x + half ) ) - max( 1, x - k + 1 )
#     return max( 0, scope - k + 1 )

# #X,X+1,...,Y,Y+1,...,N
# def d( k ):
#     if k < 2 or y == n:
#         return 0
#     half = ( y - ( x - 1 ) ) // 2
#     scope = min( ( y + k - 1 ), n ) - max( ( y - half ), ( y - k + 1 ) )
#     return max( 0, scope - k + 1 )

# for k in range(1, n):
#     ans = a(k) + b(k) + 2*c(k) + 2*d(k)
#     if k == 1:
#         ans -= 1    # A&B
#     if k > 1 and k < x + 1 and x > 1:
#         ans -= 1
#     if k > 1 and k < n - ( y - 2 ) and y < n:
#         ans -= 1
#     #print( a(k), b(k), c(k), d(k) )
#     print( max( 0, ans ) )

# 以下カンニング
ans = [ 0 ] * n
for i in range( 1, n + 1 ):
    for j in range( i + 1, n + 1 ):
        d = min( [ j - i,
                abs( x - i ) + 1 + abs( j - y ),
                abs( y - i ) + 1 + abs( j - x ) ] )
        ans[ d ] += 1

for k in range( 1, n ):
    print( ans[k] )
