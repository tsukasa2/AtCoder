import sys

sys.setrecursionlimit( 10 ** 8 )

A, B, C = map( int, input().split() )

# def search( a, b, c, r = 1, s = 0 ):
#     if a > 99 or b > 99 or c > 99:
#         return r * s
#     else:
#         return search( a + 1, b, c, r * a / ( a + b + c ), s + 1 ) + search( a, b + 1, c, r * b / ( a + b + c ), s + 1 ) + search( a, b, c + 1, r * c / ( a + b + c ), s + 1 )
    
def search( a, b, c, r = 0 ):
    if a > 99 or b > 99 or c > 99:
        return r
    else:
        next_a = a + a / ( a + b + c )
        next_b = b + b / ( a + b + c )
        next_c = c + c / ( a + b + c )
        return search( next_a, next_b, next_c, r + 1 )

# print( search( A, B, C ) )

#### 復習
exp_memo = [ [ [ -1 for _ in range( 100 ) ] for _ in range( 100 ) ] for _ in range( 100 ) ]

def expected( a, b, c ):
    if a == 100 or b == 100 or c == 100:
        return 0
    
    if exp_memo[ a ][ b ][ c ] >= 0:
        return exp_memo[ a ][ b ][ c ]
        
    exp = 0
    exp += ( expected( a + 1, b, c ) + 1 ) * a / ( a + b + c )
    exp += ( expected( a, b + 1, c ) + 1 ) * b / ( a + b + c )
    exp += ( expected( a, b, c + 1 ) + 1 ) * c / ( a + b + c )
    
    exp_memo[ a ][ b ][ c ] = exp
    return exp

print( expected( A, B, C ) )