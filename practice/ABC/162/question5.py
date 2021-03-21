from math import gcd 

n, k = input().split()
n = int( n )
k = int( k )

mod = 10 ** 9 + 7

def fact( n ):
    if n == 0:
        return 1
    elif n > 0:
        return ( n * fact( n-1 ) ) % mod
    else:
        return False

def n_gcd( n_list ):
    if len( n_list ) > 1:
        return gcd( n_list[0], n_gcd( n_list[1:] ) ) % mod
    elif len( n_list ) == 1:
        return n_list[0] % mod
    else:
        return False

#print( n_gcd( [18, 12, 36] ) )

#以下，解説を見ながら考えたもの
def g( n, k, i ):
    ret = 1
    for m in range(n):
        ret = ( ret * int( k/i ) ) % mod
    return ret

f = {}
sum_gcd = 0
for i in reversed( range( 1, k+1 ) ):
    f[i] = g( n, k, i )
    for c in range( 2, int( k / i ) + 1 ):
        f[i] = f[i] - f[ c*i ]
    sum_gcd = ( sum_gcd + i * f[i] ) % mod

#print( f )
print( sum_gcd )