A, B = map( int, input().split() )

if A == 0:
    A += 1
if B == 0:
    print( 0 )
    exit()

def count_digits( x, d ):
    # 0以上x以下の整数のうち，2^dのくらいが1になるものの数
    x += 1
    s = 2 ** ( d + 1 )
    res = ( x // s ) * s // 2
    r = x % s
    res += max( 0, r - s // 2 )
    return res

ans = ""
for i in range( 40 ):
    digit = count_digits( B, i ) - count_digits( A - 1, i )
    ans += str( digit % 2 )

print( int( ans[ ::-1 ], 2 ) )