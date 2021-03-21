import sys
sys.setrecursionlimit( 10 ** 8 )

n, k = map( int, input().split() )
s = str( input() )

def judge( a, b ):
    if a == "R" and b == "P":
        return b
    elif a == "P" and b == "S":
        return b
    elif a == "S" and b == "R":
        return b
    else:
        return a

kth_s = s + s
for _ in range( k ):
    next_s = ""
    for i in range( n ):
        next_s += judge( kth_s[ 2 * i ], kth_s[ 2 * i + 1 ] )
    kth_s = next_s + next_s

print( kth_s[ 0 ] )

# def search( l, r ):
#     if r - l == 2:
#         i = l
#         j = r - 1
#     else:
#         i = search( l, ( l + r ) // 2 )
#         j = search( ( l + r ) // 2, r )
    
#     if s[ i % n ] == "R" and s[ j % n ] == "P":
#         return j
#     elif s[ i % n ] == "P" and s[ j % n ] == "S":
#         return j
#     elif s[ i % n ] == "S" and s[ j % n ] == "R":
#         return j
#     else:
#         return i

# print( s[ search( 0, 2 ** k ) ] )