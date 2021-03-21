N = int( input() )
L = list( map( int, input().split() ) )

shorter = [ 0 for _ in range( 2100 ) ]
# shorter[ x ] = 長さx以下の棒の本数
equal = [ 0 for _ in range( 2100 ) ]
# equal[ x ] = 長さxの棒の本数

for l in L:
    equal[ l ] += 1

for i in range( 1, 2100 ):
    shorter[ i ] = shorter[ i - 1 ] + equal[ i ]

ans = 0

for a in range( N ):
    for b in range( N ):
        if a == b:
            continue
        left = abs( L[ a ] - L[ b ] )
        right = L[ a ] + L[ b ] - 1
        c = shorter[ right ] - shorter[ left ]
        if left < L[ a ] and L[ a ] <= right:
            c -= 1
        if left < L[ b ] and L[ b ] <= right:
            c -= 1 
        c = max( 0, c )
        ans += c

print( ans // 6 )